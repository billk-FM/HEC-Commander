
<p align="center">
  <img src="../misc/RAS-Commander-Logo.png" width="300">
</p>


# RAS-Commander: <br> Parallel-Execute HEC-RAS Plans

## Introduction

The RAS-Commander scripts are designed to enable parallel execution of HEC-RAS plans across multiple locally-connected machines. The scripts are intended to be run in a Jupyter notebook within VSCode, in a Microsoft Windows environment.

To get started, you need VSCode, Anaconda, and a Python 3.11 environment.  To leverage remote machines, you will need to establish a network share folder, remote desktop access, and security privileges to execute processes remotely.

Read the Quick Start Guide here: **[Quick Start Guide for RAS-Commander.pdf](./Quick%20Start%20Guide%20for%20RAS-Commander.pdf)**

---
##

## Scripts

**[RAS-Commander Parallel Execute.ipynb](./RAS-Commander%20Parallel%20Execute.ipynb)**
End-to-end handling of HEC-RAS parallel execution for all plans in a given folder.  Parallel Exectution in a native Windows environment to enable the use of latest releases. 

Author:  William Mark Katzenmeyer, P.E., C.F.M., C.H. Fenstermaker and Associates, L.L.C.

This script performs the following steps:
1. Build New Plans from DSS Inputs
2. Deploy copies to local or remote machines
3. Execute all plans in parallel
4. Collect results files back to HEC-RAS folder
5. Delete deployed copies


**[RAS-Commander Parallel Execute from DSS.ipynb](./RAS-Commander%20Parallel%20Execute%20from%20DSS.ipynb)**
End-to-end handling of HEC-RAS Calibration and Validation workflows that utilize a single DSS file input to a 1D or 2D model.  Parallel Exectution in a native Windows environment to enable the use of latest releases. 

Author:  William Mark Katzenmeyer, P.E., C.F.M., C.H. Fenstermaker and Associates, L.L.C.

This script performs the following steps:
1. Build Plan from user-specified DSS files
2. Deploy copies to local or remote machines
3. Execute all new plans in parallel
4. Collect results files back to HEC-RAS folder
5. Delete deployed copies
---

## User Inputs and Settings

Note about python paths:  Always make sure to include _r""_ in your around your paths.  Without the r, or without the quotes it will give an error

## Example input file for RAS-Commander Parallel Execute


```

#   --  INPUT HEC-RAS PROJECT FOLDER  --
# This script runs all HEC-RAS plans in parallel

# HEC-RAS Project Template Folder
HECRAS_Project_To_Run = r"Your_HECRAS_Project_with_Plans"

# Define Remote Target Folders
HECRAS_Deploy_Targets = [ 
r"C:\Local_Temp_Folder",
r"\\NetworkName1\RemoteTempFolder",
r"\\NetworkName2\RemoteTempFolder",
]  
# Accepts any combination of local and remote paths for deployment

# Define number of copies in each target (usually 2-4)
Number_Parallel_Runs = 3

# Optional step to rename DSS Outputs (Useful if using permutation plans in HEC-RAS)
Rename_DSS_Outputs = "No"  # "Yes" or "No"

# Define substring start and end positions for the new DSS file name
substring_start_position = 4
substring_end_position = 7
# For Example, a plan name with "AEP 100YR" would have it's DSS output renamed to "100YR.dss" with the above substring positions 

```


### 1. HECRAS_Project_To_Run
The HECRAS_Project_To_Run is a string that specifies the location of the HEC-RAS Project on the local machine on the local machine that you want to run. This folder should contain a HEC-RAS folder with all plans ready to run (successfully entering unsteady calculations without errors or exceptions). The path should be an absolute path to the directory.  

### 2. HECRAS_Deploy_Targets
The HECRAS_Deploy_Targets is a list of raw strings, where each string is a full path to a remote target folder. The script will deploy the generated HEC-RAS folder to these locations. It can accept any combination of local and remote paths for deployment.  Please note, only local paths and remote share paths in **\\MACHINE\FILESHARE** format are accepted.  Utilizing shared, mapped network drives (Z:\) are not supported at this time, as most modern NAS solutions will attempt to create backups and versioning of individual folder copies.  Simple Windows file sharing is recommended.  

### 3. Number_Parallel_Runs
The Number_Parallel_Runs is an integer that defines the number of HEC-RAS plans that will run in parallel on each target specified in HECRAS_Deploy_Targets. This is useful for optimizing computational resources and should be set according to the capabilities of the target machine(s).

## Additional Settings, Paths, Folder Names
```
# NOTE: Keep the outputfolder name the same as the template, there is a safety mechanism that looks at the first leters of the folder name

# ***********        FOR DEPLOY SCRIPT: HEC-RAS Version, Local Paths and File Type Exclusions           ***********

# Specify HEC-RAS EXE Path for .bat file creation (Change Version here if needed)
hecras_exe_path = r"C:\Program Files (x86)\HEC\HEC-RAS\6.2\Ras.exe"
print ("HEC-RAS Executable Path Used for batch file creation: ", hecras_exe_path) 

'''
** PSEXEC Control Options **
PSEXEC can be used to control number of cores, but requires each available core to be specified for each run
Not implemented here, but can be added by end users if needed.  Recommend using RAS option to limit # of cores instead
'''

# Flag to run PSEXEC in system account (Yes or No) (uses -s flag instead of -i {Psexec_Session_ID})
Psexec_Run_In_System_Account = "No"  # No is recommended, system account can hang without user feedback

# If not in system account, specify session ID to run in (usually 2 for single user machines) (-i {Psexec_Session_ID})
# Task Manager detail tab can be used to find Session ID on remote machine
Psexec_Session_ID = 2 

# Remote Deployment Task Priority (low, below normal, normal)
Psexec_Priority = "low" # low recommended for maximum responsiveness on multi-user machines

# Local Target Path used in Batch File Creation 
Remote_Share_Path = "C:\\"

# Build Remote_Base_Directory for batch file creation
Remote_Base_Directory = Remote_Share_Path + HECRAS_Deploy_Targets[0].split('\\', 3)[-1]
print ("Local Target Path Used for batch file creation: ", Remote_Base_Directory) 

# Folder Folder_Safety_Prefix:  This prevents the script from deleting unrelated folders 
# Specify how many of the folder prefix characters need to match  
Folder_Safety_Prefix_Length = 2

# OPTIONAL Prefix for filtering DSS files in HMS Folder (default is blank, returns all files)
# Useful if you have DSS files for multiple events in the same folder
HECHMS_dss_filter_prefix = ""

# Define exclusions for folder deployment 
# NOTE: .tif, .tiff are needed for 2D preprocessing
# For 1D, add these back for faster deployment: '*.tif', '*.tiff', '*.img',

exclusions = [ '*.p**.hdf']
print ("The following file types are not needed for 1D compute runs and will be excluded: ", exclusions)

# Number of Parallel Threads for File Copy Operations
File_Copy_Threads = 2
print ("Number of Parallel Threads for File Copy Operations: ", File_Copy_Threads)

```


### 1. hecras_exe_path
The `hecras_exe_path` is a string that points to the location of the HEC-RAS executable file (Ras.exe) on the local machine. This path is used for creating batch files that will run the HEC-RAS plans. Make sure to specify the correct version of the HEC-RAS executable for your model.

### 2. PSEXEC Control Options
The script provides settings to control PSEXEC, a tool used to execute processes on other systems. Notably:

- `Psexec_Run_In_System_Account`: A string that determines if PSEXEC should run under the system account.
- `Psexec_Session_ID`: An integer representing the Session ID to run the process in, if not in the system account.
- `Psexec_Priority`: A string indicating the priority of the process.

### 3. Remote_Share_Path
The `Remote_Share_Path` is a string that specifies the local path that corresponds to the remote share. This path is used when creating batch files for remote execution of HEC-RAS plans.

### 4. Remote_Base_Directory
The `Remote_Base_Directory` is constructed using `Remote_Share_Path` and an element from the `HECRAS_Deploy_Targets` list. It forms a directory path used in batch file creation.

### 5. Folder_Safety_Prefix_Length
The `Folder_Safety_Prefix_Length` is an integer that sets how many characters of the folder prefix need to match as a safety mechanism. This is used to prevent the script from accidentally deleting unrelated folders during its operation.

### 6. HECHMS_dss_filter_prefix
The `HECHMS_dss_filter_prefix` is an optional string that can be used to filter DSS files in the HEC-HMS input folder. If specified, only files with this prefix will be imported into the DSS. By default, this is left blank, which means all files will be imported.

### 7. exclusions
The `exclusions` is a list of strings where each string is a file extension to be excluded during the folder deployment process. For instance, files with extensions .tif or .tiff are typically not needed for 1D compute runs and can be excluded to save space and time.

### 8. File_Copy_Threads
The `File_Copy_Threads` is an integer that defines the number of parallel threads to be used for copying files. This setting is useful for optimizing the speed of file transfers during the deployment process.

### 9. Remote_File_Share_Path
The `Remote_File_Share_Path` is a string that specifies the local path corresponding to a simple remote file share. **This needs to be the same for all remote paths defined in HECRAS_Deploy_Folders.** This information is used to transform remote path strings to local path strings for remote execution, as HEC-RAS needs the full local path to run successfully.


---

## How to Run the Script

1. Download a scripts using the links above.  (Ctrl+Shift+S to download)
2. Open the Jupyter notebook inside VSCode.
3. Update the variables as described in the User Inputs and Settings section.
4. Select your Python environment created per the Quick Start Guide
5. Click "Run All" to execute all code cells.

---

## Additional Settings for the "from DSS" version of RAS-Commander

```
# HEC-RAS Project Template Folder
HECRAS_template_folder = r"C:\Your_HECRAS_Template_Folder"

# HEC-HMS Input Files
HECHMS_for_dss_import = r"C:\Your_HECHMS_Output_DSS_Folder"

#   --  OUTPUT LOCATION FOR HEC-RAS FOLDER WITH ALL PLANS --
HECRAS_output_folder = r"C:\Your_Target_For_HECRAS_Output" 

# OPTIONAL Prefix for filtering DSS files in HMS Folder (default is blank, returns all files)
# Useful if you have DSS files for multiple events in the same folder
HECHMS_dss_filter_prefix = ""
```
### 1. HECRAS_template_folder
The `HECRAS_template_folder` is a string that points to the location of the HEC-RAS project template.  This should be a template with a working RAS plan that you wish to permutate with varying DSS inputs.  This version of the script only supports a single DSS input file, and is intended to be used with the HMS-Commander script to generate calibration runs.  

### 2. HECHMS_for_dss_import
The "HECHMS_for_dss_import" is a string that points to the location of the DSS files which you would like to use to permute the HEC-RAS plans.  

### 3. HECRAS_output_folder
The `HECRAS_output_folder` is a string that points to the location of the HEC-RAS project template.  This should be a template with a working RAS plan that you wish to permute with varying DSS inputs.  This version of the script only supports a single DSS input file, and is intended to be used with the HMS-Commander script to generate calibration runs.

### 4. HECHMS_dss_filter_prefix
The `HECHMS_dss_filter_prefix` is an optional seting used to filter the files imported from HECHMS_for_dss_import.  Only files matching the prefix given by the user will be imported.  For LWI, all HMS run names start with the event name, so this is intended to allow the user to avoid moving files instead vary the prefix to select the desiried event.  Leave blank ("") if not desired.

## Contributing

If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository or send the author an email at billk@fenstermaker.com


  <img src="../misc/RAS-Commander Robot.png" width="500">


