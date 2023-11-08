# Miscellaneous Tools for HEC-RAS

**[IFA-Commander - Set all IFA to Non-Permanent.ipynb](./IFA-Commander%20-%20Set%20all%20IFA%20to%20Non-Permanent.ipynb)**
Addresses limitation of HEC-RAS by toggling all ineffective flow areas to Non-Permanent
Author: Tyler Young, E.I., C.H. Fenstermaker and Associates, L.L.C.

Purpose:
When using Rasmapper to implement IFA's, as of version 6.4 it will create all IFAs as permanent by default
Since the typical Ineffective flow area at a overtopping structure needs to be non-permanenet, this script allows changing all IFAs to non-permanent to circumvent the need for manually setting back to non-permanent any time RASMapper is used.  This script wil search and replace all values.  Future versions should include a workflow for establishing overrides for specific cross section IFA's.  


**[Folder_Submittal_File_Length_Check.ipynb](./Folder_Submittal_File_Length_Check.ipynb)**
Checks a submittal folder and reports the longest file path and remaining allowable file path characters for an NTFS file system
Author: William Katzenmeyer, P.E.., C.H. Fenstermaker and Associates, L.L.C.


**[2D_Mannings_Region_Tables_to_CSV.ipynb](./2D_Mannings_Region_Tables_to_CSV.ipynb)**
This script will output the Mannings "N" Regions defined in a 2-D HEC-RAS Geometry file and export them to CSV
ChatGPT source for script:  [Few-Shot Example: Exporting 2D Mannings Regions to CSV](https://chat.openai.com/share/5c0f6028-c7a8-4d1e-baf9-75abeb450065)
