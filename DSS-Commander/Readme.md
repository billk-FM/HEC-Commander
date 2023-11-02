<p align="center">
 <img src="../misc/DSS-Commander.png" width="300">
</p>


# DSS-Commander

DSS-Commander contains a script for plotting HEC-RAS 1D results from DSS against gauge results by creating zoomable HTML plots using Bokeh. Calibration statistics (RMSE, r, PBIAS, NSE) are also calculated for each location that is plotted.

For STAGE time series, RMSE is calculated with the mean depth of all gauged values and all other statistics are calculated using Depth
For FLOW time series, RMSE is calculated with the peak flow of all gauged values



<details>
<summary>Quick Start Guide for DSS-Commander (Expand)</summary>

*Quick Start Guide in PDF Format with screenshots: 
https://github.com/billk-FM/HEC-Commander/blob/main/Quick%20Start%20Guide%20for%20HEC-Commander.pdf

#

**Install Python using Anaconda Navigator**   
Download via **https://www.anaconda.com/**

Then, create a Python 3.11 Environment:

1. Open Anaconda Navigator  
2. Environments > Create   
3. Create Python 3.11 Environment  
4. Open a Terminal in the new environment  
5. Install Required Dependencies with this command:  


#
**Install Visual Studio Code (VSCode) + Jupyter and Python Extensions**   
Download via **https://code.visualstudio.com/Download**  

After installing, Install the following Visual Studio Code Extensions (Ctrl+Shift+X):

- Jupyer  
- Python   
- Python Environment Manager

</details>


## Example User Input Section:

The script works by filtering the DSS pathnames to create grouped plots.  The user must specify the following information:

```
# USER INPUTS: 

# DSS and Plotting Parameters
DSS_Source_Path = r"C:\Path\To_Your\DSS Results"                                            # DSS Source Path with DSS files to plot   
gauge_csv_file_name = "Gauge_Data.csv"                                                      # Gauge data file name (within root folder)     
river_stations = ["12345", "6789", "101112"]                                                # Define List of River Stations to Plot
search_word = "March"                                                                       # Enter a word from your HMS or RAS run name to filter results
plot_window_start , plot_window_end = "01APR2021 00:00:00" , "10APR2021 00:00:00"           # Example: "28MAR2018 00:00:00" , "10APR2018 00:00:00"   
base_condition_dss = "EVENT_BASE"                                                           # Time series matching this search phrase will be plotted in blue

# Time Series Type: ex. "STAGE" or "FLOW"
search_parameter1 = "STAGE"
search_parameter2 = "FLOW"

# PLOT CUSTOMIZATION
# Customization Options:
bokeh_plot_width = 1250
bokeh_plot_height = 600
bokeh_table_width = 1250
bokeh_table_height = 200

# File Names
output_html_file_name = "_Plots.html"
bokeh_plot_title = "Time Series Plots by River Station and Series Type"

# Additional Information 
# This is the bottom elevation of the river_stations mentioned above, so depth can be calculated (in the same order as the river_stations)
chan_bottom_elevation_dict = {"89804": 112.3, "117188": 79.25, "110449": 43.66}

'''For best results, ensure the gauge data and dss files fully cover the plot window.  '''
```

For multiple events, it's best to keep the DSS and Plotting Parameters copied into a markdown cell or within a docstring for later use.  Detph is used to calculate statistics for stage, so bottom depth must be provided.  



## Example Gauge_Data.csv file:

The user must provide a gauge data CSV with the same timestamps and interval as the DSS file.  This file must be in the DSS_Source_Path and the CSV file name must defined in the input section.

```Example Gauge Data CSV File:
River Station,89804,89804,117188,110449,110449
STAGE or FLOW,STAGE,FLOW,STAGE,STAGE,FLOW
Date,USGS_STA_NUM1,USGS_STA_NUM1,USGS_STA_NUM2,USGS_STA_NUM3,USGS_STA_NUM3
3/28/2018 0:00,116.8,60.7,95.195,50.146,371
3/28/2018 1:00,116.8,60.7,95.195,50.126,368
3/28/2018 2:00,116.79,60.1,95.195,50.136,369
```


