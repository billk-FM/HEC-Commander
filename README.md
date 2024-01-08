# HEC-Commander Tools

![Fenstermaker Logo](misc/fenstermaker-logo.png)

HEC-Commander Tools is a suite of python notebooks developed with AI assistance for water resource engineering workflows, primaruly focused on providing automation for HEC-RAS and HEC-HMS through jupyter notebooka with ai-assisted coding.

Developed to support Region 4 of the Louisiana Watershed Initiative by Fenstermaker.  (Not affiliated with HEC, content is exclusively third party automation utilizing publicly available software)


## Primary Author
William Mark Katzenmeyer, P.E., C.F.M.

## Notable Contributors
- [Sean Micek, P.E.](https://github.com/openSourcerer9000) - HMS-Commander Jython core logic, implementation of calibration regions
- Tyler Young, E.I. - DSS-Commander calibration metrics, debugging, and testing of all tools

For queries or further information, please contact billk@fenstermaker.com.

## Blog

Please go to the [Blog folder](https://github.com/billk-FM/HEC-Commander/tree/main/Blog)  above for archived posts!


## HMS-Commander
Contains automation scripts for HEC-HMS that allow the generation of multiple DSS output files with user-defined calibration parameters. This tool was developed to support 1D HEC-RAS calibration and validation workflows using deficit and constant loss methods with optional recession baseflow, and employs a user-generated CSV file to input scale factors for each individual parameter. Additional scripting facilitates the definition of multiple calibration regions, enabling spatially variable scale factors.

## RAS-Commander
Includes a suite of HEC-RAS automation scripts that support the parallel execution of HEC-RAS unsteady plans, as well as construction of plan files utilizing multiple HEC-HMS inputs. Defines DSS output file names, generates batch scripts for headless execution, and manages the deployment and parallel execution of HEC-RAS runs on local and remote machines using peer-to-peer Windows network shares. These scripts are applicable for both 1D and 2D model formats.

## DSS-Commander
Provides a script for plotting 1D HEC-RAS results from DSS against gauge results, creating zoomable HTML plots with Bokeh. It calculates calibration statistics (RMSE, r, PBIAS, NSE) for each plotted location and supports multiple gauges, as well as the plotting of multiple DSS results files for both Stage and Flow.

## Using ChatGPT to Understand RASCommander
Please utilize my newly published GPT that specializes in summarizing code in natural language:  [Natural Langauge Program Outline GPT]([https://www.anaconda.com/](https://chat.openai.com/g/g-c2T23DMnI-natural-language-program-outline))
With this tool, you can upload any of the notebooks from this repo and the GPT will provide a natural langage summary of its operation and important variables. The markdown can be copy/pasted to a new markdown cell in VS Code for inline documentation. 

## Quick Start Guide
<details>
<summary>Quick Start Guide for HEC-Commander Tools (Click to Expand)</summary>

**Install Python using Anaconda Navigator**   
Download via [Anaconda.com](https://www.anaconda.com/)

Then, create a Python 3.11 Environment:

1. Open Anaconda Navigator  
2. Environments > Create   
3. Name: `HEC-Env`, Packages: Search and select Python, Version: `3.11`
4. Launch a Terminal in the new environment  
5. Install required dependencies with the command: `pip install -r requirements.txt`

**Install Visual Studio Code (VSCode) + Jupyter and Python Extensions**   
Download via [Visual Studio Code](https://code.visualstudio.com/Download)

After installing VSCode:

- Open Extension View (`Ctrl+Shift+X`)
- Search and install: `Jupyter`, `Python`, `Python Environment Manager`

**Install Java Software Development Kit**
Download the JDK version 20.0.1 required for HEC-HMS 4.9 from [Oracle](https://download.oracle.com/java/20/archive/jdk-20.0.1_windows-x64_bin.msi).

**Install Jython**
Download the Jython Installer from [Jython.org](https://www.jython.org/download.html) and install to the default location (C:\jython2.7.3).

**Create Local Windows File Share for Remote Execution**
1. Log into the remote machine
2. Create a directory (e.g., `C:\RASCommander_Run`)
3. Right-click on the folder, select "Properties"
4. Go to "Sharing" tab, click "Share..."
5. Add 'Everyone' and set permissions to 'Read/Write', click "Share"

</details>
