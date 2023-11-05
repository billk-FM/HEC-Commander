<p align="center">
 <img src="../misc/HMS-Commander-Logo.png" width="300">
</p>

# HMS-Commander

Python Notebooks for automating the *HEC-HMS Hydrologic Modeling System* for *LWI Region 4*. These scripts streamline calibration workflows using methods like deficit and constant loss, Clark unit hydrograph, and recession baseflow. A white paper is also included, providing guidance on using large language models to enhance and tailor these scripts for various project-specific workflows.

---

*[Quick Start Guide in PDF Format with screenshots](https://github.com/billk-FM/HEC-Commander/blob/main/HMS-Commander/Quick%20Start%20Guide%20for%20HMS-Commander.pdf)*

---

## Scripts

### HMS-Commander - Without Calibration Regions

Automates `HEC-HMS` execution with user-defined calibration parameters. Authored by William Mark Katzenmeyer, P.E., C.F.M., C.H. Fenstermaker and Associates, L.L.C.

The script executes the following steps:
1. Read User Input CSV.
2. For each run missing output files, update:
   - Soil and Baseflow Parameters (.basin file).
   - TC and R (.basin file).
   - Output DSS file name (.run file).
   - Impervious Grids if scale > 1.0 (.grid file).
3. Execute `HEC-HMS` using `Jython`.
4. Restore files to their original state.
5. Repeat for all user-defined runs.

---

### HMS-Commander - With Calibration Regions

Includes the same functionalities as the basic version, with added capability for creating Calibration Regions.

Authored by William Mark Katzenmeyer, P.E., C.F.M., C.H. Fenstermaker and Associates, L.L.C.

This script includes the following steps:
1. Read User Input CSV.
2. Read Calibration Regions Shapefile.
3. Assign a calibration region for each subbasin.
4. For each run missing output files, update parameters as listed above.
5. Execute `HEC-HMS` using `Jython`.
6. Restore files to their original state.
7. Repeat for all user-defined runs.

---

### Quick Start Guide for HEC-Commander

*Ensure Jython is installed at the default location: `C:\jython2.7.3\`*

Use a Python 3.9 environment or higher, with the correct Java SDK version for your `HEC-HMS` version as tested with `HEC-HMS 4.9`, `Jython 2.4.3`, and `Java SDK 20.0.1`.

### Prepare the Run Parameters CSV

The example CSV provided defines input parameters for HMS model runs. Microsoft Excel is recommended for CSV file editing.

#### CSV Format Example:

| user_run_number_from_csv | initial_deficit_scale | maximum_deficit_scale | ... | storage_coefficient_scale |
|--------------------------|-----------------------|-----------------------|-----|---------------------------|
| 1                        | 1.0                   | 1                     | ... | 1                         |
| 2                        | 0.9                   | 1                     | ... | 1                         |

*Parameters in the CSV correspond with `.basin` file entries, with additional scaling applied by the script.*

### Baseflow Parameters Handling

If "None" is set for Baseflow in the basin file, user-defined values for baseflow parameters are inserted by the script.

### Impervious Scaling

Care is taken to prevent scaling impervious layers above 100%. The script requires corresponding `.dss` files for scale factors greater than 1.0 in the project directory.

### File Backup, Restore, and Locking

A system to backup, restore, and lock files is implemented to protect against data loss during script execution. Users should verify their `.basin` file if the script is interrupted.

### Run Control by Output File Presence

Run execution is controlled by the presence of output DSS files. Deleting an output file allows for re-execution of that specific run with updated parameters.

---

## Additional Instructions for HMS-Commander with Calibration Regions

Requires a Python 3.11 environment for the use of Geopandas.

### Changes to Input CSV for Calibration Zones

The CSV format is extended to include `calregion`, which corresponds with the Calibration Regions shapefile.

#### CSV Format Example with Calibration Zones:

| user_run_number_from_csv | calregion | initial_deficit_scale | ... | storage_coefficient_scale |
|--------------------------|-----------|-----------------------|-----|---------------------------|
| 1                        | 1         | 0.99                  | ... | 1.1                       |
| ...                      | ...       | ...                   | ... | ...                       |

### Producing a Calibration Regions Shapefile

Instructions for creating and using a Calibration Regions shapefile in ArcGIS are provided in the guide.

### Additional Resources

* [HEC-HMS User's Manual](https://www.hec.usace.army.mil/software/hec-hms/documentation.aspx)
* [Python and HMS-Commander White Paper](https://github.com/billk-FM/HEC-Commander/blob/main/HMS-Commander/White%20Paper%20on%20Python%20Scripts%20for%20HMS.pdf)

---

