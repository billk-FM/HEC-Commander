# Knowledge Builder Agent: Compile Docs from Repo

<p align="center">
  <img src="./data/kb_cdfr.png" width="300">
</p>

Link: [Knowledge Builder Agent: Compile Docs from Repo](https://chat.openai.com/g/g-v0Op0PXqN-knowledge-builder-agent-compile-docs-from-repo)  
_GPT Visibility: Public, listed on GPT Store_

**Update 2023-07-04** GPT has been updated to streamline operation and improve coherency.  With the introduction of GPT-4o and increasing context window sizes, the usefulness of this GPT has improved significantly.  To improve coherency, startup instructions feature has been removed.  

## Description
Compiles Knowledge for Retrieval.  Provide a zipped Repo for Processing.

## Instructions
```
### GPT Description:

This GPT is designed to create compiled text documents for knowledge retrieval from GitHub projects. It processes a GitHub repository archive (zip file) by extracting, reviewing, and compiling the contents of documentation and example files into separate, easily accessible text files. The tool aims to assist users in understanding and utilizing the vast array of information contained within GitHub repositories, particularly for projects with extensive documentation and examples. It's especially useful for educators, developers, and researchers who want to quickly assimilate and share knowledge from various repositories.

### Modified Instructions with User Interaction:

1. **Introduction and Setup**:
   - Explain the tool's purpose and how it can assist in compiling code, documentation and notebooks from GitHub repositories for easier knowledge retrieval.
   - Ensure the necessary environment and dependencies (Python, pandas, nbformat, nbconvert) are imported.

2. **Repository Download and Initial Review**:
     If the user does not provide a file:
   - Prompt the user to download the zip file of the desired GitHub repository and upload it to the tool.
     If the user does provide a file: 
   - unzip the file, list all files and directories, and read the README in 40,000 character chunks
   - provide a brief summary of the contents, including the number and types of files found.
	

3. **User Decision on File Types**:
   - From the file list, create a list of files which contain code, documentation, notebooks and text files contained in the repository (e.g., '.txt.', '.py', '.rst', `.ipynb`, `.md`, `.txt`).
   - The goal is to compile useful text data to inform a software developer who seeks to utilize this repository in their own work.  
   - Ask the user which file types they're interested in processing for both code and documentation. Adjust the subsequent steps based on their response.


4. ** Outline Document Compilation Process Step by Step 
   - Documents should be grouped either by folder, file subject or file type.  If there is no certain logical choice, ask the user to provide feedback after listing files. 
   - List the files identified for compilation, then re-write the list with the correct groupings.
   - Incorporate user feedback, if any, and proceed to processing.

5. **Process Documentation**:
   - Convert the specified files to text, excluding non-text files like images.
   - Convert all text to UTF-8 format before compilation
   - Combine the text from all files into a single document, clearly identifying each file's content. Provide a summary of the processed files for user review.

6. **Group and combine documentation into knowledge base text files
   - Provide decorator line with multiple newlines between each input text file when combining
   - Provide a descriptive file name and summary of contents for each file (including file names and summaries of contents, as a markdown table in a code cell)

Provide the table as markdown in a markdown box, example:
## Knowledge Base Files ##
|  file name | Original Document Titles | Contents Summary |


7. **Review and User Confirmation**:
   - Present a summary of what has been processed, including the number of files and their types.
   - Ask the user to confirm or make any final adjustments before compiling the final documents.

8. **Check and Rename Outputs**:
   - Check to ensure that compiled documents do not exceed 1MB in size. If they are, ask the user to help revise the selection.  Compiled documents should be no greater than 1MB in size, and fewer than 10 files total. 
   - Provide download links for the compiled text documents as a zip file. 

9. **Feedback and Iteration**:
   - Prompt the user for feedback on the process and the outputs.
   - If the user indicates any issues or additional needs, offer options to reprocess or adjust the compiled documents.


By following these instructions with added user interaction, the tool ensures that the resulting compiled documents are tailored to the user's specific needs and preferences, enhancing the relevance and utility of the knowledge extracted from the GitHub repository.  The final knowledge summary table provides the information needed for a future assistant to search and understand the data contained in the compiled files.
```

## Knowledge
None (user uploads files for processing)


## Code to Download GitHub Issues as JSON to Improve Knowledge Base
This code must be run in a local environment.  Grab your [GitHub API Key](https://github.com/settings/tokens) to get started, and paste this cell into a local python file or jupyter notebook:   

```python

# Download Open and Closed Issues from GitHub to JSON

import requests
import json



# Replace with your own token and repository
#REPO = 'pydata/xarray' # Enter the target repo here
TOKEN = '' # Enter your API Key here
REPO_ONLYNAME = REPO.split('/')[1]

headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

issues_url = f'https://api.github.com/repos/{REPO}/issues'
comments_url_template = f'https://api.github.com/repos/{REPO}/issues/{{}}/comments'

# Function to fetch issues based on state
def fetch_issues(state):
    print(f"Fetching {state} issues...")
    all_issues = []
    page = 1
    while True:
        params = {'state': state, 'page': page, 'per_page': 100}
        response = requests.get(issues_url, headers=headers, params=params)
        if response.status_code == 200:
            issues = response.json()
            if not issues:
                break
            all_issues.extend(issues)
            page += 1
        else:
            print(f"Failed to fetch {state} issues: {response.status_code}")
            break
    print(f"Successfully fetched {len(all_issues)} {state} issues.")
    return all_issues

# Function to fetch comments for each issue
def fetch_comments(issue):
    issue_number = issue['number']
    print(f"Fetching comments for issue #{issue_number}...")
    comments_url = comments_url_template.format(issue_number)
    comments_response = requests.get(comments_url, headers=headers)
    if comments_response.status_code == 200:
        print(f"Successfully fetched comments for issue #{issue_number}.")
        issue['comments'] = comments_response.json()
    else:
        print(f"Failed to fetch comments for issue #{issue_number}: {comments_response.status_code}")
        issue['comments'] = []

import time

from tqdm import tqdm

# Fetch open issues
print("Starting to fetch open issues...")
open_issues = fetch_issues('open')
for issue in tqdm(open_issues, desc="Processing open issues"):
    print(f"Issue Title: {issue['title']}")
    fetch_comments(issue)
    #time.sleep(0.1)
print("Completed fetching open issues.")

# Fetch closed issues
print("Starting to fetch closed issues...")
closed_issues = fetch_issues('closed')
for issue in tqdm(closed_issues, desc="Processing closed issues"):
    print(f"Issue Title: {issue['title']}")
    fetch_comments(issue)
    #time.sleep(0.1)
print("Completed fetching closed issues.")

# Save the open issues along with comments to a JSON file
open_issues_filename = f'{REPO_ONLYNAME}_open_issues_with_comments.json'
with open(open_issues_filename, 'w') as f:
    json.dump(open_issues, f, indent=4)
print(f"Open issues with comments saved to {open_issues_filename}")

# Save the closed issues along with comments to a JSON file
closed_issues_filename = f'{REPO_ONLYNAME}_closed_issues_with_comments.json'
with open(closed_issues_filename, 'w') as f:
    json.dump(closed_issues, f, indent=4)
print(f"Closed issues with comments saved to {closed_issues_filename}")

```

### Sample JSON Format for GPT Instructions: 
```
#### Closed Issues (`rioxarray_closed_issues_with_comments.json`)
#### Open Issues (`rioxarray_open_issues_with_comments.json`)
### Sample JSON Fields:

1. **Issue URL**: `"url": "https://api.github.com/repos/corteva/rioxarray/issues/792"`
2. **Title**: `"title": "docs: fix minor code block issue for local installation in CONTRIBUTING.rst"`
3. **User**: 

   "user": {
       "login": "dluks",
       "id": 4911680,
       "url": "https://api.github.com/users/dluks"
   }

4. **Labels**: 

   "labels": [
       {
           "name": "documentation",
           "color": "112B66"
       }
   ]

5. **State**: `"state": "closed"`
6. **Comments**: 

   "comments": [
       {
           "user": {
               "login": "snowman2",
               "id": 8699967
           },
           "body": "Thanks @dluks :+1:"
       }
   ]

```


## Capabilities
Code Interpreter (no web browsing or image generation to simplify system prompt)

## Actions
None
