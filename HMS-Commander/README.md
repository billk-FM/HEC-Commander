<p align="center">
 <img src="../misc/HMS-Commander-Logo.png" width="300">
</p>

# HMS-Commander

Python Notebooks for automating HEC-HMS Hydrologic Modeling System initially developed for LWI Region 4. The provided scripts automate calibration workflows for HEC-HMS models utilizing deficit and constant loss methods, clark unit hydrograph and recession baseflow methods. A white paper is also provided in this repository with examples of how to leverage large language models to edit and extend these scripts for other project-specific workflows.

*[Quick Start Guide in PDF Format with screenshots](https://github.com/billk-FM/HEC-Commander/blob/main/HMS-Commander/Quick%20Start%20Guide%20for%20HMS-Commander.pdf)*

---

## Scripts

### [HMS-Commander - Without Calibration Regions.ipynb](./HMS-Commander%20-%20Without%20Calibration%20Regions.ipynb)

End-to-end handling of HEC-HMS automated execution for a set of calibration parameters that can be defined by the user as an input CSV file.

Author: William Mark Katzenmeyer, P.E., C.F.M., C.H. Fenstermaker and Associates, L.L.C.

This script performs the following steps:

1. Read User Input CSV
2. For each user-defined run whose output file is missing, update the following:
   - Soil and Baseflow Parameters (.basin file)
   - TC and R (.basin file)
   - Output DSS file name (.run file)
   - Impervious Grids if scale >1.0 (.grid file)
3. Execute HEC-HMS using Jython
4. Restore files
5. Repeat until all user runs have been executed

---

### [HMS-Commander - With Calibration Regions.ipynb](./HMS-Commander%20-%20With%20Calibration%20Regions.ipynb)

Same features as HMS-Commander, with the ability to create Calibration Regions

Author: William Mark Katzenmeyer, P.E., C.F.M., C.H. Fenstermaker and Associates, L.L.C.

This script performs the following steps:

1. Read User Input CSV
2. Read Calibration Regions Shapefile
3. Determine calibration region for each subbasin
4. For each user-defined run whose output file is missing, update the following:
   - Soil and Baseflow Parameters (.basin file)
   - TC and R (.basin file)
   - Output DSS file name (.run file)
   - Impervious Grids if scale >1.0 (.grid file)
5. Execute HEC-HMS using Jython
6. Restore files
7. Repeat until all user runs have been executed

---

### Quick Start Guide for HEC-Commander

*Quick Start Guide in PDF Format with screenshots: [https://github.com/billk-FM/HEC-Commander/blob/main/Quick%20Start%20Guide%20for%20HEC-Commander.pdf](https://github.com/billk-FM/HEC-Commander/blob/main/Quick%20Start%20Guide%20for%20HEC-Commander.pdf)*

**You must ensure that Jython is installed to the default location**: `C:\jython2.7.3\`

Please use a Python 3.9 environment or higher, and ensure you have the correct version of the Java SDK installed for the version of HEC-HMS you have specified in the script. The script has been tested with HEC-HMS 4.9, Jython 2.4.3 and Java SDK 20.0.1, per the Quick Guide.

---

### Prepare the Run Parameters CSV

The following example input CSV has been provided:

| user_run_number_from_csv | initial_deficit_scale | maximum_deficit_scale | percolation_rate_scale | impervious_area_scale | recession_factor | initial_flow_area_ratio | threshold_flow_to_peak_ratio | time_of_concentration_scale | storage_coefficient_scale |
|--------------------------|-----------------------|-----------------------|------------------------|-----------------------|------------------|-------------------------|------------------------------|-----------------------------|---------------------------|
|                        1 |                   1.0 |                     1 |                   0.06 |                     1 |              0.1 |                       1 |                          0.1 |                           1 |                         1 |
|                        2 |                   0.9 |                     1 |                   0.06 |                     1 |              0.1 |                       1 |                          0.1 |                           1 |                         1 |

The parameters in the CSV are defined as follows:

- `initial_deficit_scale`: Scaling factor for initial deficit.
- `maximum_deficit_scale`: Scaling factor for maximum deficit.
- `percolation_rate_scale`: Scaling factor for percolation rate.
- `impervious_area_scale`: Scaling factor for impervious area.
- `recession_factor`: Recession curve factor.
- `initial_flow_area_ratio`: Ratio of initial flow to area.
- `threshold_flow_to_peak_ratio`: Threshold of flow to peak flow ratio.
- `time_of_concentration_scale`: Scaling factor for time of concentration.
- `storage_coefficient_scale`: Scaling factor for storage coefficient.

Please follow the Quick Start Guide for more detailed instructions on how to prepare your input CSV file.
