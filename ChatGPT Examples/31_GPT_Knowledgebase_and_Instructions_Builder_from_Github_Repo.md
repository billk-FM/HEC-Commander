# GPT Knowledge and Instructions Builder (from Github Repo)

Link to Notebook: [GPT_Knowledgebase_and_Instructions_Builder_from_Github.ipynb](https://github.com/billk-FM/HEC-Commander/blob/e093f55c6bfd36c6ad72de7a099e8e7f1bd24a4e/ChatGPT%20Examples/data/GPT_Knowledgebase_and_Instructions_Builder_from_Github.ipynb)

## Overview

The GPT Knowledge Builder is a tool designed to compile GitHub repositories into a knowledgebase suitable for use with GPT Assistants. This project helps users create concise, well-structured knowledge bases that meet specific requirements:

- Less than 10 files
- Less than 5 million tokens per file or 512MB

## Prerequisites

To use this tool, you'll need:

1. GitHub API Key (stored in `GH_API_Token.txt`)
2. OpenAI API Key (stored in `OAI_API_Key.txt`)

Place these files in the same folder as the script, with the API keys inside.

## Features

- Downloads and processes GitHub repositories
- Compiles repository contents into manageable knowledge base files
- Handles various file types, including conversion of some formats to markdown
- Downloads and processes GitHub Issues and Comments
- Generates summaries of the knowledge base using GPT models
- Creates custom instructions for GPT assistants based on the repository content

## Usage

1. Set up the required API keys in the appropriate files.
2. Modify the user input section to specify the repository, subfolders, and exclusions.
3. Run the notebook cells sequentially to process the repository and generate the knowledge base.

## Key Components

- Repository download and processing
- File type handling and conversion
- Token counting and cost estimation
- LLM-based summarization of repository contents
- Custom instruction generation for GPT assistants

## Output

The tool produces several outputs, including:

- Processed repository files
- Compiled knowledge base files
- Summarized knowledge base content
- Custom instructions for GPT assistants

## Notes

- The tool uses various models, including GPT-4 and GPT-4-mini, for different tasks.
- Cost estimations are provided to help manage API usage.
- The final output is optimized for use with Claude, an AI assistant.

## Dependencies

The script uses several Python libraries, including but not limited to:

- gitpython
- tqdm
- pandas
- matplotlib
- networkx
- openai
- transformers

These dependencies are automatically installed if missing.

## Disclaimer

This tool interacts with external APIs and processes large amounts of data. Be mindful of API usage limits and costs associated with using language models.

## Detailed Usage Example

Let's use the repository "billk-FM/HEC-Commander" as an example to demonstrate how to set up the user input block.

### User Input Block

```python
# User Input for Repository, Subfolders and Exclusions

# Specify the GitHub repository to process
REPO = 'billk-FM/HEC-Commander'

# Define the list of subfolders to process
# Use ["ALL"] to process all subfolders in the repository
subfolders = ["ALL"]
# Example of specific subfolders: subfolders = ["doc", "hvplot", "examples"]

# Read the GitHub API token from a file
from pathlib import Path
token_file_path = Path('GH_API_Token.txt')
with token_file_path.open('r') as file:
    TOKEN = file.read().strip()

# Define file extensions to exclude from processing
file_exclusions = {
    '.png', '.jpg', '.jpeg', '.shp', '.geojson', '.gpkg', '.dll', '.zip', '.svg', 
    '.csv', '.tiff', '.tif', '.bmp', '.gif', '.hdf', '.h5', '.nc', '.kml', '.kmz', 
    '.grib', '.grb', '.grb2', '.bin', '.exe', '.iso', '.ico', '.arrow', '.parquet', 
    '.feather', '.pickle', '.dbf', '.shx', '.ipch', '.db', '.lib', 'heclib.a', '.JPG', '.qgs', 
    '.mldata', '.cpg', '.qss', '.gpx', '.dxf', '.qgz', '.mailmap', '.gitmodules', '.gitignore', '.dockerignore', 'hydrus', '.pas', '.svg',
}

# Define directories to exclude from processing
dir_exclusions = {
    '.git', '.github', 'tests', '.circleci', 'gitpod', '_static', 'zlib', 'staticdata', 
    'test', 'fonts', 'outdated_wheels', 'output', 'data', '.coverage_dir', 'licenses', 
    'benchmarks', 'other', '.devcontainer', 'img'
}

# Define subfolder for LLM summary output
llm_chunked_summary_subfolder = "llm_chunked_summaries"

# Configuration for downloading GitHub Issues
download_comments = True  # Set to False to skip downloading comments
closed_issues_limit = 10000  # Maximum number of closed issues to download
closed_issues_cutoff_year = 2000  # Earliest year to consider for closed issues

# Limit the number of chunks for LLM summarization (0 for unlimited)
max_llm_chunks = 0

```

### Explanation of User Inputs

1. `REPO`: 
   - Purpose: Specifies the GitHub repository to process.
   - Example: 'billk-FM/HEC-Commander'
   - Explanation: This is the full path of the repository on GitHub, including the username or organization name.

2. `subfolders`:
   - Purpose: Defines which subfolders of the repository to process.
   - Example: ["ALL"]
   - Explanation: Using ["ALL"] processes all subfolders. You can specify individual subfolders if needed, e.g., ["doc", "examples"].

3. `TOKEN`:
   - Purpose: Reads the GitHub API token from a file for authentication.
   - Example: Reads from 'GH_API_Token.txt'
   - Explanation: This token is used to authenticate API requests to GitHub, allowing access to the repository.

4. `file_exclusions`:
   - Purpose: Defines file types to exclude from processing.
   - Example: Includes various file extensions like .png, .jpg, .csv, etc.
   - Explanation: These file types are typically binary or large data files that aren't useful for text-based knowledge bases.

5. `dir_exclusions`:
   - Purpose: Specifies directories to exclude from processing.
   - Example: Includes directories like .git, tests, data, etc.
   - Explanation: These directories often contain non-essential information for the knowledge base or test files.

6. `llm_chunked_summary_subfolder`:
   - Purpose: Defines the subfolder where LLM summary outputs will be stored.
   - Example: "llm_chunked_summaries"
   - Explanation: This is where the tool will save summarized chunks of the knowledge base.

7. `download_comments`:
   - Purpose: Determines whether to download comments from GitHub Issues.
   - Example: True
   - Explanation: When set to True, the tool will download and process comments from GitHub Issues.

8. `closed_issues_limit`:
   - Purpose: Sets the maximum number of closed issues to download.
   - Example: 10000
   - Explanation: This limits the number of closed issues processed, which can be useful for large repositories.

9. `closed_issues_cutoff_year`:
   - Purpose: Sets the earliest year from which to consider closed issues.
   - Example: 2000
   - Explanation: This allows you to exclude very old issues that might not be relevant anymore.

10. `max_llm_chunks`:
    - Purpose: Limits the number of chunks for LLM summarization.
    - Example: 0 (unlimited)
    - Explanation: Setting this to a non-zero value limits the amount of text processed by the language model, which can be useful for very large repositories or to control costs.

By configuring these inputs, you can tailor the tool's behavior to the specific needs of the HEC-Commander repository or any other repository you're working with. This setup allows for flexible processing of repository content, enabling you to create a focused and relevant knowledge base for your GPT assistant.
