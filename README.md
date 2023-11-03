# HEC-Commander Tools by
<p align="center">
  <a href="https://Fenstermaker.com/">
    <img alt="Fenstermaker Logo" width="300" src="misc/fenstermaker-logo.png" />
  </a>
</p>




HEC-Commander tools is a suite of Tools for HEC-RAS and HEC-HMS Automation, designed for Water Resource Engineers.  All scripts contained in this repository were initially developed by William Katzenmeyer, P.E., C.F.M. at C.H. Fenstermaker and Associates, LLC for use in Region 4 of the Louisiana Watershed Initiative.   

>
>### Primary Author:  
>William Mark Katzenmeyer, P.E., C.F.M.
>
>### Notable Contributors:
>Sean Micek, P.E. (HMS-Commander jython core logic, Implementation of Calibration Regions)
>
>Tyler Young, E.I. (DSS-Commander Calibration Metrics, Debugging and Testing of all tools)

## DSS-Commander 
DSS-Commander contains a script for plotting HEC-RAS 1D results from DSS against gauge results by creating zoomable HMTML plots using Bokeh.  Calibration statistics (RMSE, r, PBIAS, NSE) are also calculated for each location that is plotted.  Supports multiple gauge and plotting of multilpe DSS results files, Stage and Flow. 

## HMS-Commander 
HMS-Commander contains automation scripts for HEC-HMS that allows the generation of multiple DSS output files with user-defined calibration parameters.  This tool was developed to support 1D HEC-RAS calibration and validation workflows using deficit and constant loss methods with optional recession baseflow, using a user-generated CSV file to input scale factors for each individual parameter.  An additional script is included which allows for the definition of multiple calibration regions to allow spatially varying scale factors.



## RAS-Commander 
RAS-Commander contains a series of HEC-RAS automation scripts that allow the building of plan files utilizing mutliple HEC-HMS inputs, Defining DSS output file names, generating Batch Scripts for headless execution, as well as deployment and parallel execution of HEC-RAS runs on local and remote machines using peer to peer windows network shares.  These scripts can be leveraged for 1D as well as 2D models.  Individual scripts are provided in case flexibility is needed for model configurations, as well as "Fully Auto" scripts that handle end to end processing for specific workflows utilized during the Louisiana Watershed Initiative.     


<details>
<summary>Quick Start Guide for HEC-Commander Tools (Click to Expand)</summary>

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

#
**Install Java Software Development Kit**
Download latest version via  **https://download.oracle.com/java/20/archive/jdk-20.0.1_windows-x64_bin.msi**
NOTE:  For HEC-HMS 4.9, JDK version 20.0.1 must be installed.   


#
**Install Jython**
Download Jython Installer via **https://www.jython.org/download.html**
Install to the default location (C:\jython2.7.3)

#

**Create Local Windows File Share to Support Remote Execution**
1. Log into the remote machine
2. Create a folder (Example: C:\RASCommander_Run)
3. Right click folder and go to “Properties” 
4. Navigate to “Sharing” tab and click “Share”						         
5. Add read/write user permissions for each user or user group that will be executing runs remotely

Note:  When setting up multiple machines for remote execution, ensure that each shared folder is placed at the same path on each machine, preferably outside of the user profile folders.  

#

Now your environment is set up to run scripts in the HEC-Commander repository! Other necessary files will be installed from within the jupyter notebooks as needed.  

Contact you IT department or edit the script if you can't do the following:
- Create folders on your C:\ drive
- Log in to remote machines with Remote Desktop
- Create local file shares using Windows File Sharing

These are not absolutely required, but are highly recommended (or make edits to the script paths as needed to accomodate your setup).  Without the creation of local file shares, remote execution is not possible without reconfiguring the script for using mapped, shared network drives. 

</details>

