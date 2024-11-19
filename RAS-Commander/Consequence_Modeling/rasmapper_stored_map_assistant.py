# rasmapper_layer_inserter.py

import subprocess
import sys
import os
import queue
import time
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import xml.etree.ElementTree as ET
import shutil
import logging
import threading
import psutil  # Lightweight library for process management
import h5py  # For HDF file manipulation

# Setup logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Formatter for logging
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

def update_hdf_terrain_reference(hdf_path, terrain_name):
    """
    Updates the terrain reference in an HDF file's Geometry group.
    
    Parameters:
        hdf_path (Path): Path to the HDF file
        terrain_name (str): Name of the selected terrain
    """
    try:
        with h5py.File(hdf_path, 'r+') as f:
            if 'Geometry' in f:
                geom = f['Geometry']
                # Update terrain attributes if they exist
                if 'Terrain Filename' in geom.attrs:
                    terrain_path = f".\\Terrain\\{terrain_name}.hdf"
                    geom.attrs.modify('Terrain Filename', terrain_path.encode())
                if 'Terrain Layername' in geom.attrs:
                    geom.attrs.modify('Terrain Layername', terrain_name.encode())
                logger.info(f"Updated terrain references in HDF file: {hdf_path}")
    except Exception as e:
        logger.error(f"Failed to update terrain reference in HDF file {hdf_path}: {e}")
        raise

def update_terrain_section(rasmap_file, terrain_name):
    """
    Updates the Terrains section in the RASMAP file to ensure the selected terrain is checked.
    
    Parameters:
        rasmap_file (Path): Path to the RASMAP file
        terrain_name (str): Name of the selected terrain
    """
    tree = ET.parse(rasmap_file)
    root = tree.getroot()
    
    terrains = root.find('Terrains')
    if terrains is not None:
        # Find the selected terrain layer
        for layer in terrains.findall('Layer'):
            if layer.get('Name') == terrain_name:
                layer.set('Checked', 'True')
            else:
                layer.set('Checked', 'False')
        
        # Ensure Terrains element is checked and expanded
        terrains.set('Checked', 'True')
        terrains.set('Expanded', 'True')
        
        tree.write(rasmap_file, encoding='utf-8', xml_declaration=True)
        logger.info(f"Updated terrain section in RASMAP file for terrain: {terrain_name}")

def backup_and_filter_terrains(rasmap_file, selected_terrain):
    """
    Creates a backup of the original RASMAP file and removes all terrains except the selected one.
    
    Parameters:
        rasmap_file (Path): Path to the RASMAP file
        selected_terrain (str): Name of the terrain to keep
        
    Returns:
        Path: Path to the backup file
        list: List of XML elements representing removed terrains
    """
    backup_file = rasmap_file.with_suffix('.rasmap.backup')
    shutil.copy2(rasmap_file, backup_file)
    
    tree = ET.parse(rasmap_file)
    root = tree.getroot()
    
    terrains_elem = root.find('Terrains')
    if terrains_elem is None:
        return backup_file, []
    
    removed_terrains = []
    for terrain in terrains_elem.findall('Layer'):
        if terrain.get('Name') != selected_terrain:
            removed_terrains.append(terrain)
            terrains_elem.remove(terrain)
    
    tree.write(rasmap_file, encoding='utf-8', xml_declaration=True)
    logger.info(f"Temporarily removed {len(removed_terrains)} terrain(s) from RASMAP file")
    
    return backup_file, removed_terrains

def restore_terrains_from_backup(rasmap_file, backup_file):
    """
    Restores the original RASMAP file from backup.
    
    Parameters:
        rasmap_file (Path): Path to the RASMAP file
        backup_file (Path): Path to the backup file
    """
    try:
        shutil.copy2(backup_file, rasmap_file)
        backup_file.unlink()  # Remove backup file
        logger.info("Restored original RASMAP file with all terrains")
    except Exception as e:
        logger.error(f"Failed to restore RASMAP file from backup: {e}")
        raise

class QueueProcessor:
    def __init__(self, message_queue, text_widget, root):
        self.message_queue = message_queue
        self.text_widget = text_widget
        self.root = root
        self.running = True

    def process_queue(self):
        """Process messages from the queue and update the text widget"""
        if not self.running:
            return

        try:
            while True:  # Process all available messages
                message = self.message_queue.get_nowait()
                self.text_widget.configure(state='normal')
                self.text_widget.insert(tk.END, message + '\n')
                self.text_widget.configure(state='disabled')
                self.text_widget.see(tk.END)
                self.text_widget.update_idletasks()  # Force update
                self.message_queue.task_done()
        except queue.Empty:
            pass

        if self.running:
            self.root.after(100, self.process_queue)

    def stop(self):
        """Stop the queue processor"""
        self.running = False

# Stream handler for logging to terminal box
class GuiHandler(logging.Handler):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget
        self.setFormatter(formatter)  # Use the formatter defined at module level

    def emit(self, record):
        msg = self.format(record)
        # Update the text widget directly from the main thread
        self.text_widget.configure(state='normal')
        self.text_widget.insert(tk.END, msg + '\n')
        self.text_widget.configure(state='disabled')
        self.text_widget.see(tk.END)
        self.text_widget.update_idletasks()  # Force update

# Utility Functions

def extract_terrain_names(rasmap_file):
    """
    Extracts terrain names from the Terrains section of a RASMAP file.

    Parameters:
        rasmap_file (str): Path to the RASMAP file.

    Returns:
        list of str: List of terrain names.
    """
    if not os.path.isfile(rasmap_file):
        raise FileNotFoundError(f"The file '{rasmap_file}' does not exist.")

    try:
        tree = ET.parse(rasmap_file)
        root = tree.getroot()
    except ET.ParseError as e:
        raise ValueError(f"Failed to parse the RASMAP file. Ensure it is a valid XML file. Error: {e}")

    terrains = root.find('Terrains')
    if terrains is None:
        raise ValueError("The RASMAP file does not contain a 'Terrains' section.")

    terrain_names = [layer.get('Name') for layer in terrains.findall('Layer') if layer.get('Name')]
    logger.info(f"Extracted terrain names: {terrain_names}")
    return terrain_names

def create_map_definition(name, map_type, filename, profile_name, terrain=None, additional_params=None):
    """
    Creates a dictionary representing a stored map definition.

    Parameters:
        name (str): Name of the map.
        map_type (str): Type of the map (e.g., "elevation", "velocity").
        filename (str): Path to the map file.
        profile_name (str): Profile name associated with the map.
        terrain (str, optional): Terrain name. If provided, overrides StoredFilename with terrain-specific path.
        additional_params (dict, optional): Any additional map parameters.

    Returns:
        dict: Stored map definition.
    """
    map_params = {
        "MapType": map_type,
        "OutputMode": "Stored Current Terrain",
        "StoredFilename": filename,
        "ProfileIndex": "2147483647",
        "ProfileName": profile_name
    }

    # If terrain is specified, adjust the StoredFilename accordingly
    if terrain:
        base, ext = os.path.splitext(filename)
        filename = os.path.join(os.path.dirname(filename), f"{base}_{terrain}{ext}")
        map_params["StoredFilename"] = filename

    # Include any additional parameters
    if additional_params:
        map_params.update(additional_params)

    return {
        "name": name,
        "type": "RASResultsMap",
        "checked": True,
        "filename": filename,
        "map_parameters": map_params
    }

def insert_stored_maps(rasmap_file, stored_maps, terrain=None):
    """
    Inserts stored map definitions into each RASResults Layer within the Results section of a RASMAP file.
    Also updates terrain references in associated HDF files.
    """
    rasmap_file = Path(rasmap_file)
    if not rasmap_file.is_file():
        raise FileNotFoundError(f"The file '{rasmap_file}' does not exist.")

    # Create a backup of the original file
    backup_file = rasmap_file.with_suffix(rasmap_file.suffix + '.bak')
    shutil.copyfile(rasmap_file, backup_file)
    logger.info(f"Backup of the original file created at '{backup_file}'.")

    try:
        tree = ET.parse(rasmap_file)
        root = tree.getroot()
    except ET.ParseError as e:
        raise ValueError(f"Failed to parse the RASMAP file. Ensure it is a valid XML file. Error: {e}")

    results = root.find('Results')
    if results is None:
        raise ValueError("The RASMAP file does not contain a 'Results' section.")

    rasresults_layers = results.findall("Layer[@Type='RASResults']")
    if not rasresults_layers:
        logger.warning("No RASResults Layers found in the Results section. No maps were inserted.")
        return

    for rasresults_layer in rasresults_layers:
        rasresults_name = rasresults_layer.get('Name', 'Unnamed RASResults')
        logger.info(f"Processing RASResults Layer: '{rasresults_name}'")

        # Update HDF terrain reference if needed
        hdf_filename = rasresults_layer.get('Filename')
        if hdf_filename and hdf_filename.lower().endswith('.hdf'):
            hdf_path = Path(rasmap_file).parent / hdf_filename
            if hdf_path.exists() and terrain:
                try:
                    update_hdf_terrain_reference(hdf_path, terrain)
                except Exception as e:
                    logger.warning(f"Could not update terrain reference in HDF file {hdf_path}: {e}")

        for stored_map in stored_maps:
            map_name = stored_map['name']
            
            # Find existing map layers with matching name
            existing_layers = rasresults_layer.findall(f".//Layer[@Name='{map_name}']")
            
            # Check if any of the existing layers are stored maps (have Filename attribute and StoredFilename in MapParameters)
            stored_layer_exists = False
            for existing_layer in existing_layers:
                map_params = existing_layer.find('MapParameters')
                if (map_params is not None and 
                    existing_layer.get('Filename') and 
                    map_params.get('OutputMode') == 'Stored Current Terrain' and
                    map_params.get('StoredFilename')):
                    stored_layer_exists = True
                    # Update terrain if specified
                    if terrain:
                        map_params.set('Terrain', terrain)
                        logger.info(f"  - Updated existing stored map '{map_name}' with terrain '{terrain}' under RASResults Layer '{rasresults_name}'")
                    break

            # Only create new stored map if no stored version exists
            if not stored_layer_exists:
                # Create new stored map layer
                map_parameters = stored_map['map_parameters'].copy()
                if terrain:
                    map_parameters['Terrain'] = terrain
                    logger.info(f"  - Terrain '{terrain}' specified. Updating map parameters for '{map_name}'.")

                # Create a new Layer element for stored map
                layer_elem = ET.Element('Layer')
                layer_elem.set('Name', map_name)
                layer_elem.set('Type', stored_map['type'])
                layer_elem.set('Checked', 'True')
                
                # Set the Filename attribute based on the RASResults folder name
                results_folder = rasresults_name.replace(" ", "_")
                filename = f".\\{results_folder}\\{map_name} (Max).vrt"
                layer_elem.set('Filename', filename)
                map_parameters['StoredFilename'] = filename

                # Create MapParameters sub-element
                map_params_elem = ET.SubElement(layer_elem, 'MapParameters')
                for param_key, param_value in map_parameters.items():
                    map_params_elem.set(param_key, str(param_value))

                # Append the new Layer to the RASResults Layer
                rasresults_layer.append(layer_elem)
                logger.info(f"  - Inserted new stored map '{map_name}' under RASResults Layer '{rasresults_name}'.")

    try:
        tree.write(rasmap_file, encoding='utf-8', xml_declaration=True)
        logger.info(f"RASMAP file '{rasmap_file}' has been updated successfully.")
    except Exception as e:
        raise IOError(f"Failed to write changes to the RASMAP file. Error: {e}")

def define_default_stored_maps(terrain=None):
    """
    Defines default stored maps (WSEL, Velocity, Depth).

    Parameters:
        terrain (str, optional): Terrain name to specify in map parameters.

    Returns:
        list of dict: List of stored map definitions.
    """
    stored_maps = [
        create_map_definition(
            name="WSEL",
            map_type="elevation",
            filename="./Grid Precip Infiltration/WSEL.vrt",
            profile_name="Max",
            terrain=terrain,
            additional_params={"LayerName": "Water Surface Elevation"}
        ),
        create_map_definition(
            name="Velocity",
            map_type="velocity",
            filename="./Grid Precip Infiltration/Velocity.vrt",
            profile_name="Max",
            terrain=terrain
        ),
        create_map_definition(
            name="Depth",
            map_type="depth",
            filename="./Grid Precip Infiltration/Depth.vrt",
            profile_name="Max",
            terrain=terrain
        )
    ]
    return stored_maps

def parse_rasmap_results(rasmap_file):
    """
    Parses the Results section of the RASMAP file to extract plan file names.
    Only includes plans where the HDF file exists on disk.

    Parameters:
        rasmap_file (str or Path): Path to the RASMAP file.

    Returns:
        list of str: List of plan file names without the .hdf extension.
    """
    rasmap_file = Path(rasmap_file)
    if not rasmap_file.is_file():
        raise FileNotFoundError(f"The file '{rasmap_file}' does not exist.")

    try:
        tree = ET.parse(rasmap_file)
        root = tree.getroot()
    except ET.ParseError as e:
        raise ValueError(f"Failed to parse the RASMAP file. Ensure it is a valid XML file. Error: {e}")

    results = root.find('Results')
    if results is None:
        raise ValueError("The RASMAP file does not contain a 'Results' section.")

    plan_files = []
    for layer in results.findall(".//Layer[@Type='RASResults']"):
        filename = layer.get('Filename')
        if filename and filename.lower().endswith('.hdf'):
            # Convert the HDF path to absolute path relative to the RASMAP file
            hdf_path = Path(rasmap_file.parent / filename)
            if hdf_path.is_file():
                plan_name = Path(filename).stem  # Remove .hdf extension
                plan_files.append(plan_name)
            else:
                logger.warning(f"Skipping non-existent HDF file: {hdf_path}")

    logger.info(f"Found {len(plan_files)} existing plan files: {plan_files}")
    return plan_files

def update_run_flags(plan_file_path, flags, terminal_box=None):
    """Updates the run flags in a HEC-RAS plan file."""
    plan_file_path = Path(plan_file_path)
    if not plan_file_path.is_file():
        raise FileNotFoundError(f"The plan file '{plan_file_path}' does not exist.")

    flag_mapping = {
        'geometry_preprocessor': 'Run HTab',
        'unsteady_flow_simulation': 'Run UNet',
        'run_sediment': 'Run Sediment',
        'floodplain_mapping': 'Run RASMapper'
    }

    original_flags = {}
    changes_made = False

    try:
        # Read the file content
        with open(plan_file_path, 'r') as file:
            lines = file.readlines()

        # Process each line
        for i, line in enumerate(lines):
            for key, file_key in flag_mapping.items():
                if key in flags and flags[key] is not None and line.strip().startswith(file_key):
                    original_value = line.strip().split('=')[-1].strip()
                    original_flags[key] = original_value
                    new_value = '1' if flags[key] else '0'
                    
                    if original_value != new_value:
                        lines[i] = f"{file_key}= {new_value}\n"
                        changes_made = True
                        if terminal_box:
                            terminal_box.insert(tk.END, f"Updated {file_key} from {original_value} to {new_value} in {plan_file_path.name}\n")
                            terminal_box.see(tk.END)

        # Only write if changes were made
        if changes_made:
            with open(plan_file_path, 'w') as file:
                file.writelines(lines)
            logger.info(f"Successfully updated run flags in plan file: {plan_file_path}")
        else:
            logger.info(f"No changes needed for plan file: {plan_file_path}")

        return original_flags

    except IOError as e:
        logger.error(f"Error updating run flags in plan file {plan_file_path}: {e}")
        raise

def restore_run_flags(plan_file_path, original_flags, terminal_box=None):
    """
    Restores the original run flags in a HEC-RAS plan file.

    Parameters:
        plan_file_path (str or Path): Full path to the plan file.
        original_flags (dict): Original flag settings to restore.
        terminal_box (scrolledtext.ScrolledText, optional): Terminal box to display messages.

    Returns:
        None
    """
    plan_file_path = Path(plan_file_path)
    if not plan_file_path.is_file():
        raise FileNotFoundError(f"The plan file '{plan_file_path}' does not exist.")

    flag_mapping = {
        'geometry_preprocessor': 'Run HTab',
        'unsteady_flow_simulation': 'Run UNet',
        'run_sediment': 'Run Sediment',
        'floodplain_mapping': 'Run RASMapper'
    }

    try:
        with open(plan_file_path, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            for key, file_key in flag_mapping.items():
                if key in original_flags and line.strip().startswith(file_key):
                    original_value = original_flags[key]
                    lines[i] = f"{file_key}= {original_value}\n"
                    if terminal_box:
                        terminal_box.insert(tk.END, f"Restored {file_key} to {original_value} in {plan_file_path.name}\n")
                        terminal_box.see(tk.END)

        with open(plan_file_path, 'w') as file:
            file.writelines(lines)

        logger.info(f"Successfully restored run flags in plan file: {plan_file_path}")

    except IOError as e:
        logger.error(f"Error restoring run flags in plan file {plan_file_path}: {e}")
        raise

def open_hec_ras_project(ras_exe_path, project_prj_path, rasmap_file, terminal_box=None):
    """
    Opens the HEC-RAS project in Ras.exe, adjusts run flags, and provides user prompts.

    Parameters:
        ras_exe_path (str or Path): Path to Ras.exe.
        project_prj_path (str or Path): Path to the .prj file.
        rasmap_file (str or Path): Path to the .rasmap file.
        terminal_box (scrolledtext.ScrolledText, optional): Terminal box to display messages.

    Returns:
        None
    """
    ras_exe_path = Path(ras_exe_path)
    project_prj_path = Path(project_prj_path)
    rasmap_file = Path(rasmap_file)

    if not ras_exe_path.is_file():
        messagebox.showerror("Error", f"Ras.exe not found at {ras_exe_path}")
        return

    if not project_prj_path.is_file():
        messagebox.showerror("Error", f"Project .prj file not found at {project_prj_path}")
        return

    selected_terrain = self.selected_terrain.get()
    if not selected_terrain:
        messagebox.showerror("Error", "Please select a terrain.")
        return

    # Backup RASMAP and remove other terrains
    try:
        self.backup_file, removed_terrains = backup_and_filter_terrains(self.rasmap_file, selected_terrain)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to modify RASMAP file: {e}")
        return

    # Parse rasmap to get plan file names
    try:
        plan_names = parse_rasmap_results(rasmap_file)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return

    # Define flags to set
    flags_to_set = {
        'geometry_preprocessor': False,
        'unsteady_flow_simulation': False,
        'run_sediment': False,
        'floodplain_mapping': True
    }

    # Define flags to restore after RAS is closed
    original_flags_dict = {}

    # Update run flags
    for plan_name in plan_names:
        plan_file_path = project_prj_path.parent / f"{plan_name}"
        try:
            original_flags = update_run_flags(plan_file_path, flags_to_set, terminal_box)
            original_flags_dict[plan_file_path] = original_flags
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update run flags for {plan_file_path.name}: {e}")
            return

    # Launch HEC-RAS
    try:
        subprocess.Popen([str(ras_exe_path), str(project_prj_path)])
        logger.info(f"Opened HEC-RAS project: {project_prj_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open HEC-RAS: {e}")
        return

    # Prompt user to run Unsteady Calculations
    messagebox.showinfo("HEC-RAS Opened", "HEC-RAS has been opened. Please run the Unsteady Calculations (Run Multiple) to create floodplain mapping results.\n\nAfter closing HEC-RAS, the script will restore the original run flags.")

    # Wait for Ras.exe to close
    def wait_for_ras():
        # Wait until Ras.exe is closed
        ras_process = None
        while True:
            time.sleep(1)
            for proc in psutil.process_iter(['exe']):
                if proc.info['exe'] and Path(proc.info['exe']).resolve() == ras_exe_path.resolve():
                    ras_process = proc
                    break
            else:
                break  # Ras.exe not found, exit loop

        # Restore terrains first
        if hasattr(self, 'backup_file'):
            try:
                restore_terrains_from_backup(self.rasmap_file, self.backup_file)
            except Exception as e:
                logger.error(f"Failed to restore terrains: {e}")

        # Restore run flags
        for plan_file, original_flags in original_flags_dict.items():
            try:
                restore_run_flags(plan_file, original_flags, terminal_box)
            except Exception as e:
                logger.error(f"Failed to restore run flags for {plan_file.name}: {e}")
        # Notify user
        if terminal_box:
            terminal_box.insert(tk.END, "Run flags and terrains have been restored.\n")
            terminal_box.see(tk.END)
        messagebox.showinfo("HEC-RAS Closed", "HEC-RAS has been closed. Run flags and terrains have been restored.\n\nYou can now open the project folder to check the results.")
        # Open project folder in Explorer
        subprocess.Popen(['explorer', str(project_prj_path.parent)])

    # Run the wait in a separate thread to prevent GUI freezing
    threading.Thread(target=wait_for_ras, daemon=True).start()

# GUI Application

class RASMapperLayerInserter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.is_closing = False
        self.after_ids = []  # Keep track of all after callbacks
        
        self.title("RASMapper Stored Map Production Assistant")
        self.geometry("700x600")
        self.resizable(False, False)

        # Initialize variables
        self.rasmap_file = None
        self.project_prj_path = None
        self.terrain_names = []
        self.selected_terrain = tk.StringVar()
        self.maps_to_add = {
            "WSEL": tk.BooleanVar(value=True),
            "Velocity": tk.BooleanVar(value=True),
            "Depth": tk.BooleanVar(value=True)
        }
        self.ras_exe_path = tk.StringVar(value=r"C:\Program Files (x86)\HEC\HEC-RAS\6.6\Ras.exe")

        # Add tracking for RAS process and monitoring thread
        self.ras_process = None
        self.monitor_thread = None
        
        # Create UI components first
        self.create_widgets()
        
        # Initialize message queue and queue processor after terminal_box is created
        self.message_queue = queue.Queue()
        self.queue_processor = QueueProcessor(self.message_queue, self.terminal_box, self)
        self.queue_processor.process_queue()
        
        # Bind the window close event
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Setup logging to terminal box
        gui_handler = GuiHandler(self.terminal_box)
        logger.addHandler(gui_handler)
        
        # Log initial message to verify logging is working
        logger.info("Application started. Ready for input.")

    def create_widgets(self):
        padding = {'padx': 10, 'pady': 10}

        # RAS Project Folder Selection
        folder_frame = ttk.LabelFrame(self, text="HEC-RAS Project Folder")
        folder_frame.pack(fill="x", **padding)

        self.folder_path = tk.StringVar()
        folder_entry = ttk.Entry(folder_frame, textvariable=self.folder_path, width=60)
        folder_entry.pack(side="left", padx=(10, 5), pady=5)

        browse_button = ttk.Button(folder_frame, text="Browse", command=self.browse_folder)
        browse_button.pack(side="left", padx=5, pady=5)

        # Terrain Selection
        terrain_frame = ttk.LabelFrame(self, text="Select Terrain")
        terrain_frame.pack(fill="x", **padding)

        self.terrain_dropdown = ttk.Combobox(terrain_frame, textvariable=self.selected_terrain, state="readonly")
        self.terrain_dropdown.pack(fill="x", padx=10, pady=5)

        # Stored Map Layers to Add
        maps_frame = ttk.LabelFrame(self, text="Stored Map Layers to Add")
        maps_frame.pack(fill="x", **padding)

        for map_name, var in self.maps_to_add.items():
            cb = ttk.Checkbutton(maps_frame, text=map_name, variable=var)
            cb.pack(anchor='w', padx=20, pady=2)

        # Settings Frame
        settings_frame = ttk.LabelFrame(self, text="Settings")
        settings_frame.pack(fill="x", **padding)

        ras_exe_label = ttk.Label(settings_frame, text="Ras.exe Path:")
        ras_exe_label.pack(side="left", padx=(10, 5), pady=5)

        ras_exe_entry = ttk.Entry(settings_frame, textvariable=self.ras_exe_path, width=50)
        ras_exe_entry.pack(side="left", padx=5, pady=5)

        browse_ras_button = ttk.Button(settings_frame, text="Browse", command=self.browse_ras_exe)
        browse_ras_button.pack(side="left", padx=5, pady=5)

        # Action Buttons
        action_frame = ttk.Frame(self)
        action_frame.pack(fill="x", **padding)

        add_button = ttk.Button(action_frame, text="Step 1:\nAdd Selected Maps", command=self.add_maps)
        add_button.pack(side="left", expand=True, fill="x", padx=10)

        open_ras_button = ttk.Button(action_frame, text="Step 2:\nOpen Project in HEC-RAS for Floodplain Mapping", command=self.open_project_in_ras)
        open_ras_button.pack(side="left", expand=True, fill="x", padx=10)

        exit_button = ttk.Button(action_frame, text="Close HEC-RAS and Exit", command=self.on_closing)
        exit_button.pack(side="left", expand=True, fill="x", padx=10)

        # Terminal Box
        terminal_frame = ttk.LabelFrame(self, text="Program Terminal")
        terminal_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.terminal_box = scrolledtext.ScrolledText(
            terminal_frame,
            wrap=tk.WORD,
            height=10,
            font=('Consolas', 9)
        )
        self.terminal_box.pack(fill="both", expand=True, padx=5, pady=5)
        self.terminal_box.configure(state='disabled')

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)
            self.project_prj_path = self.find_prj_file(folder_selected)
            self.load_rasmap()

    def find_prj_file(self, project_folder):
        prj_candidates = list(Path(project_folder).glob("*.prj"))
        if not prj_candidates:
            logger.error("No .prj file found in the selected folder.")
            messagebox.showerror("Error", "No .prj file found in the selected folder.")
            return None
        
        # If we have multiple .prj files, try to match with .rasmap name
        if len(prj_candidates) > 1:
            # Find the .rasmap file first
            rasmap_candidates = list(Path(project_folder).glob("*.rasmap"))
            if rasmap_candidates:
                rasmap_name = rasmap_candidates[0].stem  # Get name without extension
                # Look for matching .prj file
                for prj_file in prj_candidates:
                    if prj_file.stem == rasmap_name:
                        logger.info(f"Found matching .prj file: {prj_file.name}")
                        return prj_file
                
            logger.warning("Multiple .prj files found, none matching .rasmap name. Using the first one.")
            messagebox.showwarning("Warning", "Multiple .prj files found, none matching .rasmap name. Using the first one.")
        
        return prj_candidates[0]

    def browse_ras_exe(self):
        ras_exe_selected = filedialog.askopenfilename(
            title="Select Ras.exe",
            filetypes=[("Executable Files", "*.exe")],
            initialdir=r"C:\Program Files (x86)\HEC\HEC-RAS\6.6"
        )
        if ras_exe_selected:
            self.ras_exe_path.set(ras_exe_selected)

    def load_rasmap(self):
        project_folder = Path(self.folder_path.get())
        rasmap_candidates = list(project_folder.glob("*.rasmap"))
        if not rasmap_candidates:
            messagebox.showerror("Error", "No RASMAP file found in the selected folder.")
            self.terrain_dropdown['values'] = []
            self.rasmap_file = None
            return
        elif len(rasmap_candidates) > 1:
            messagebox.showwarning("Warning", "Multiple RASMAP files found. Using the first one.")
        self.rasmap_file = rasmap_candidates[0]
        try:
            self.terrain_names = extract_terrain_names(self.rasmap_file)
            self.terrain_dropdown['values'] = self.terrain_names
            if self.terrain_names:
                self.terrain_dropdown.current(0)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.terrain_dropdown['values'] = []
            self.terrain_names = []

    def add_maps(self):
        if not self.rasmap_file:
            messagebox.showerror("Error", "Please select a valid HEC-RAS project folder containing a RASMAP file.")
            return

        terrain = self.selected_terrain.get()
        if not terrain:
            messagebox.showerror("Error", "Please select a terrain.")
            return

        # Define which maps to add based on user selection
        selected_maps = []
        if self.maps_to_add["WSEL"].get():
            selected_maps.append("WSEL")
        if self.maps_to_add["Velocity"].get():
            selected_maps.append("Velocity")
        if self.maps_to_add["Depth"].get():
            selected_maps.append("Depth")

        if not selected_maps:
            messagebox.showinfo("Info", "No maps selected to add.")
            return

        # Define stored maps to insert
        stored_maps = define_default_stored_maps(terrain=terrain)
        # Filter maps based on user selection
        maps_to_insert = [m for m in stored_maps if m['name'] in selected_maps]

        try:
            insert_stored_maps(self.rasmap_file, maps_to_insert, terrain=terrain)
            messagebox.showinfo("Success", f"Selected maps have been added to '{self.rasmap_file.name}'.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to insert maps: {e}")

    def create_plans_table(self, plan_names):
        """
        Creates a formatted table showing plan numbers and their associated results layer names.
        
        Parameters:
            plan_names (list): List of plan names from the RASMAP file
            
        Returns:
            str: Formatted table as string
        """
        # Get results layer names for each plan
        table_rows = []
        tree = ET.parse(self.rasmap_file)
        root = tree.getroot()
        results = root.find('Results')
        
        if results is not None:
            for layer in results.findall(".//Layer[@Type='RASResults']"):
                plan_name = Path(layer.get('Filename', '')).stem
                if plan_name in plan_names:
                    layer_name = layer.get('Name', 'Unnamed')
                    table_rows.append(f"{plan_name}\t{layer_name}")
        
        if table_rows:
            header = "Plan Number\tResults Layer Name\n" + "-" * 50 + "\n"
            return header + "\n".join(table_rows)
        return "No plans with results found."

    def create_info_window(self, table_text):
        """
        Creates a non-blocking info window with plan information and close button.
        """
        info_window = tk.Toplevel(self)
        info_window.title("Plans Ready for Floodplain Mapping")
        info_window.geometry("500x400")
        
        # Make window stay on top
        info_window.transient(self)
        info_window.attributes('-topmost', True)
        
        # Add message and table
        message_label = ttk.Label(
            info_window, 
            text="The following plans have results files and are prepared for floodplain mapping.\n"
                 "Run or Run Multiple to Compute Stored Maps:",
            wraplength=450
        )
        message_label.pack(padx=10, pady=10)
        
        # Add table in a scrolled text widget
        table_text_widget = scrolledtext.ScrolledText(
            info_window, 
            wrap=tk.WORD, 
            width=60, 
            height=15,
            font=('Courier', 9)
        )
        table_text_widget.insert(tk.END, table_text)
        table_text_widget.configure(state='disabled')
        table_text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Add close button
        close_button = ttk.Button(
            info_window,
            text="Close HEC-RAS and Return to Main Window",
            command=lambda: self.close_ras_and_info(info_window)
        )
        close_button.pack(padx=10, pady=10)
        
        return info_window

    def close_ras_and_info(self, info_window):
        """
        Closes HEC-RAS and the info window.
        """
        # Close the info window
        info_window.destroy()
        
        # Terminate RAS process
        if self.ras_process:
            try:
                pid = self.ras_process.pid
                parent = psutil.Process(pid)
                for child in parent.children(recursive=True):
                    child.kill()
                parent.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
                pass

    def open_project_in_ras(self):
        if not self.rasmap_file:
            messagebox.showerror("Error", "Please select a valid HEC-RAS project folder containing a RASMAP file.")
            return

        if not self.project_prj_path or not self.project_prj_path.is_file():
            messagebox.showerror("Error", "Project .prj file not found. Ensure it exists in the project folder.")
            return

        selected_terrain = self.selected_terrain.get()
        if not selected_terrain:
            messagebox.showerror("Error", "Please select a terrain.")
            return

        # Create mapping backup after any stored maps are added but before terrain modifications
        try:
            self.mapping_backup = self.create_mapping_backup(self.rasmap_file)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create mapping backup: {e}")
            return

        # Backup RASMAP and remove other terrains
        try:
            self.backup_file, removed_terrains = backup_and_filter_terrains(self.rasmap_file, selected_terrain)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to modify RASMAP file: {e}")
            return

        # Parse rasmap to get plan file names
        try:
            plan_names = parse_rasmap_results(self.rasmap_file)
            if not plan_names:
                messagebox.showerror("Error", "No plan files found in the RASMAP file.")
                return
            
            # Create and show non-blocking info window
            table_text = self.create_plans_table(plan_names)
            self.info_window = self.create_info_window(table_text)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to parse RASMAP file: {e}")
            return

        # Define flags to set
        flags_to_set = {
            'geometry_preprocessor': False,
            'unsteady_flow_simulation': False,
            'run_sediment': False,
            'floodplain_mapping': True
        }

        # Store original flags for each plan file
        self.original_flags_dict = {}

        # Update run flags for all plan files
        for plan_name in plan_names:
            # Construct the exact plan file path
            plan_file = self.project_prj_path.parent / plan_name
            
            if not plan_file.exists():
                logger.error(f"Plan file not found: {plan_file}")
                continue

            logger.info(f"Processing plan file: {plan_file}")
            
            try:
                # Try to open the file first to verify we have write access
                with open(plan_file, 'r+') as f:
                    pass
                
                original_flags = update_run_flags(plan_file, flags_to_set, self.terminal_box)
                self.original_flags_dict[plan_file] = original_flags
                logger.info(f"Successfully updated run flags for plan: {plan_file.name}")
                
                # Verify the file was actually modified
                modified_time = plan_file.stat().st_mtime
                logger.info(f"Plan file {plan_file.name} modified time: {time.ctime(modified_time)}")
                
            except PermissionError:
                logger.error(f"Permission denied accessing plan file: {plan_file}")
                messagebox.showerror("Error", f"Permission denied accessing plan file: {plan_file}")
                self.restore_all_flags()
                return
            except Exception as e:
                logger.error(f"Failed to update run flags for {plan_file.name}: {e}")
                messagebox.showerror("Error", f"Failed to update run flags for {plan_file.name}: {e}")
                self.restore_all_flags()
                return

        try:
            # Launch RAS with quotes around paths
            cmd = [f'"{self.ras_exe_path.get()}"', f'"{str(self.project_prj_path)}"']
            self.ras_process = subprocess.Popen(" ".join(cmd), shell=True)
            
            # Start monitoring thread
            self.monitor_thread = threading.Thread(target=self.monitor_ras_process, daemon=True)
            self.monitor_thread.start()
            
            logger.info("HEC-RAS process started successfully")
            
            if self.terminal_box:
                self.terminal_box.insert(tk.END, f"Opening project in HEC-RAS...\n")
                self.terminal_box.see(tk.END)

        except Exception as e:
            logger.error(f"Failed to open project in HEC-RAS: {e}")
            messagebox.showerror("Error", f"Failed to open project in HEC-RAS: {e}")
            self.restore_all_flags()

    def monitor_ras_process(self):
        """Monitor RAS process and handle cleanup when it closes"""
        if self.ras_process:
            self.ras_process.wait()
            
            # Close the info window if it exists
            if hasattr(self, 'info_window') and self.info_window:
                self.info_window.destroy()
            
            # Restore from mapping backup
            if hasattr(self, 'mapping_backup'):
                try:
                    shutil.copy2(self.mapping_backup, self.rasmap_file)
                    self.mapping_backup.unlink()  # Remove the backup file
                    logger.info("Restored RASMAP file from mapping backup")
                except Exception as e:
                    logger.error(f"Failed to restore from mapping backup: {e}")

            # Restore run flags and show completion message
            if hasattr(self, 'original_flags_dict'):
                for plan_file, original_flags in self.original_flags_dict.items():
                    try:
                        restore_run_flags(plan_file, original_flags, self.terminal_box)
                    except Exception as e:
                        logger.error(f"Failed to restore run flags for {plan_file.name}: {e}")

            if not self.is_closing:  # Only show messages if not in process of closing
                self.terminal_box.insert(tk.END, "Run flags and RASMAP file have been restored.\n")
                self.terminal_box.see(tk.END)
                messagebox.showinfo("HEC-RAS Closed", "HEC-RAS has been closed. Run flags and RASMAP file have been restored.\n\nYou can now open the project folder to check the results.")
                subprocess.Popen(['explorer', str(self.project_prj_path.parent)])

    def on_closing(self):
        """Handle application closing"""
        self.is_closing = True
        
        # Force terminate RAS process if it exists
        if self.ras_process:
            try:
                # Get the process ID
                pid = self.ras_process.pid
                
                # Kill the process and all its children using psutil
                parent = psutil.Process(pid)
                for child in parent.children(recursive=True):
                    child.kill()
                parent.kill()
                
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
                pass  # Process already terminated or access denied
            
        # Destroy the window and exit immediately
        self.destroy()
        sys.exit(0)

    def create_mapping_backup(self, rasmap_file):
        """
        Creates a backup of the RASMAP file specifically for mapping operations.
        
        Parameters:
            rasmap_file (Path): Path to the RASMAP file
            
        Returns:
            Path: Path to the mapping backup file
        """
        mapping_backup = rasmap_file.with_suffix('.mapping.bak')
        shutil.copy2(rasmap_file, mapping_backup)
        logger.info(f"Created mapping backup at {mapping_backup}")
        return mapping_backup

# Main Execution

def main():
    app = RASMapperLayerInserter()
    app.mainloop()

if __name__ == "__main__":
    main()
