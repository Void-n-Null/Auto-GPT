import os
from pathlib import Path
import json

# Get the path of the current file's directory
file_dir = Path(__file__).parent.parent

# Set the path to the plugins directory
plugins_dir = file_dir / "plugins"

# List all directories in the plugins directory
plugin_folders = os.listdir(plugins_dir)

# Loop through each directory and load the manifest.json file
for folder in plugin_folders:
    manifest_file = plugins_dir / folder / "manifest.json"
    if manifest_file.exists():
        # Load the manifest file
        with open(manifest_file, "r") as f:
            manifest: dict = json.load(f)
            
        # Import any modules specified in the manifest file
        for python_file in manifest.get("python_files",[]):
            print(python_file)
            code = open(plugins_dir / folder / python_file, "r").read()
            eval(code)
