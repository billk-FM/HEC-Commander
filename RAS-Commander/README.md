# RAS-Commander
## Enhanced Single Notebook for Parallel-Executing HEC-RAS Plans

---

<p align="center">
  <img src="../misc/RAS-Commander-Logo.png" width="300">
</p>

---

## Introduction

RAS-Commander has evolved to offer a more integrated and flexible solution for the parallel execution of HEC-RAS plans. This advanced tool is now encapsulated within a single Jupyter notebook, catering to various operational needs while maintaining the core functionality of efficiently managing HEC-RAS plans across multiple machines.

Prerequisites for using RAS-Commander include VSCode, Anaconda, and a Python 3.11 environment, in addition to the necessary network configurations for remote execution.

For detailed instructions and setup, please refer to the **[Quick Start Guide for RAS-Commander.pdf](./Quick%20Start%20Guide%20for%20RAS-Commander.pdf)**.

---

## Features

### Operational Modes
The new version introduces two primary operation modes:

1. **Run Missing**: Targets and executes plans that are missing from the HEC-RAS output folder within an existing project.
2. **Build from DSS**: Builds and executes plans from a HEC-RAS template folder based on DSS file inputs.

### User-Friendly Input Structure
The notebook begins with a user inputs section, allowing for a more organized and straightforward setup. These inputs, set as defaults, can be overridden through the GUI for enhanced flexibility.

---

## How to Run

1. Download the updated script: **[RAS-Commander _1.0.ipynb](./RAS-Commander%20_1.0.ipynb)**
2. Open the notebook in VSCode.
3. Select the desired operation mode and update the necessary inputs.
4. Ensure your Python environment is set as advised in the Quick Start Guide.
5. Run the notebook to initiate the chosen operation.

---

## Changelog

- **2024-02-13**: Integrated functionalities into a single notebook with "Run Missing" and "Build from DSS" modes; Improved user input structure for enhanced usability.

---

## Contributing

Encounter any issues or have suggestions? Please open an issue on the GitHub repository or reach out to the author at billk@fenstermaker.com.

<p align="center">
  <img src="../misc/RAS-Commander Robot.png" width="500">
</p>
