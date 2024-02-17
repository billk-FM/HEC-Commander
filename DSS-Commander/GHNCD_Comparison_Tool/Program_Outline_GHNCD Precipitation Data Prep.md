### Comprehensive Summary of Jupyter Notebook: GHNCD Precipitation Data Preparation

#### Code Cell 1: User-Defined Inputs
This code cell is dedicated to defining various user-defined inputs for a data preparation process related to precipitation data. It sets up:
- `watershed_files_directory`: Directory path for watershed-related files.
- `buffer_distance_miles`: Radius in miles for filtering stations.
- `timeperiod_start` and `timeperiod_end`: Start and end dates for data collection period.
- `download_station_data`: Flag to control GHNCD data download from NOAA.
- `concurrent_downloads`: Number of concurrent downloads allowed.
- `exclude_stations_by_name`: List to exclude certain stations by name.

#### Code Cell 2: Installing and Importing Libraries
Focuses on installing and importing various Python libraries required for the precipitation data preparation script. Key actions:
- Sets an environment variable for GDAL library.
- Creates a list `packages` of Python packages to be used in the script.
- Defines `install` function to install packages using `pip` or `conda`.
- Imports necessary libraries for the script.
- Handles the GDAL library installation specific to the system and Python version.

#### Code Cell 3: Define All Paths
Dedicated to defining and setting up various file paths and directories needed for the script's operation:
- Locates the watershed boundary shapefile in `watershed_files_directory`.
- Defines function `ensure_directory_exists` to create directories if they don't exist.
- Sets up directory paths for various components like GHCND data, index files, CSV files, and precipitation outputs.

#### Code Cell 4: Downloading GHCND Station Data from AWS
Handles the downloading and initial processing of the GHCND station data from AWS:
- Constructs a path for the GHCND stations text file and checks its existence.
- Downloads the file from AWS if it doesn't exist, and processes the data into a DataFrame `stations_df`.
- Filters out invalid or missing data points from `stations_df`.

#### Code Cell 5: Finding Stations within Watershed Boundary and Buffer Distance
Focused on identifying weather stations from the GHCND dataset that fall within a specified buffer distance from a watershed boundary:
- Loads the watershed boundary shapefile into a GeoDataFrame `boundary_gdf`.
- Converts station data into a GeoDataFrame `stations_gdf`.
- Defines `haversine` function to calculate distances.
- Defines `filter_stations` function to identify stations within the buffer distance.
- Saves the result to a CSV file and visualizes the filtered stations on a plot.

#### Code Cell 6: Downloading Data for Filtered Stations
Manages the downloading of climate data for the filtered stations:
- Sets up the base URL for downloading station data.
- Downloads GHCND documentation PDF if it doesn't exist.
- Defines `download_station` function for downloading station data.
- Uses a `ThreadPoolExecutor` for concurrent downloads.
- Creates DataFrames for successful and failed downloads.

#### Code Cell 7: Parsing GHCND Stations File
Focused on parsing the `ghcnd-stations.txt` file into a DataFrame `ghcnd_stations_df`:
- Defines `parse_ghcnd_stations` function for parsing the file with fixed-width column formatting.
- Creates a DataFrame with columns for station ID, Latitude, Longitude, Elevation, and Name.

#### Code Cell 8: Creating DataFrames from AWS CSV Files
Processes the downloaded CSV files, focusing on precipitation data:
- Initializes a dictionary `dataframes_dict` to store DataFrames created from each CSV file.
- Reads each CSV file into a DataFrame, filters for precipitation data, and merges it with station details.
- Filters the DataFrames based on precipitation data and specified date range.
- Creates a DataFrame `filtered_stations_df` listing stations that meet the criteria.
- Displays relevant information from the corresponding DataFrames for each filtered station.

#### Code Cell 9: Plotting Watershed and Stations
Visualizes the watershed boundary and the stations with precipitation data:
- Creates a new figure and axis for plotting.
- Plots the watershed boundary and the locations of the filtered stations.
- Checks for data coverage adequacy and adjusts the axis limits.

#### Code Cell 10: Creating a Cleaned DataFrame with Precipitation Data
Focused on creating a consolidated DataFrame with all relevant precipitation data:
- Filters DataFrames to include only those with precipitation data.
- Initializes an empty DataFrame `prcp_time_series_df`.
- Consolidates data from different stations into `prcp_time_series_df`.
- Saves the consolidated DataFrame to a CSV file.

#### Code Cell 11: Plotting Precipitation Time Series for All Stations
Visualizes the precipitation data as a time series for each station:
- Creates a new figure and axis for plotting.
- Plots the precipitation data over time for each station.
- Adds labels, title, and legend to the plot.
- Adjusts layout for better readability and displays the plot.
