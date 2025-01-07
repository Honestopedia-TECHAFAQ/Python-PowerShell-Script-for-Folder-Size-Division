# Folder Divider Script

This Python script divides folders from a specified source directory into multiple sets of specified sizes. It's designed to work on Windows operating systems and ensures efficient handling of large datasets.

## Features
- Divide folders into sets with a specified number of folders per set.
- Creates organized subdirectories for each set.
- Automatically handles directory creation and file copying.

## Prerequisites
1. **Python**: Ensure Python 3.x is installed on your Windows machine. [Download Python](https://www.python.org/downloads/)
2. **Permissions**: Ensure you have read and write permissions for the source and target directories.

## How to Use

### Step 1: Clone or Download the Script
Save the script as `divide_folders.py` on your local machine.

### Step 2: Install Python (if not already installed)
- Open a browser and visit the [Python Downloads](https://www.python.org/downloads/) page.
- Download and install the latest version for Windows.
- During installation, check the box to "Add Python to PATH."

### Step 3: Prepare Your Directories
- Create a source directory containing the folders you want to divide.
- Choose a target directory where the sets will be created.

### Step 4: Update the Script
Edit the following variables in the `main()` function:
- `source_directory`: Set this to the path of your source directory.
- `target_directory`: Set this to the path of your target directory.
- `folders_per_set`: Define the number of folders per set.

Example:
```python
source_directory = "C:\\Users\\YourUsername\\SourceFolders"
target_directory = "C:\\Users\\YourUsername\\TargetSets"
folders_per_set = 10
