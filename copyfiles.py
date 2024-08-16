import os
import shutil
from datetime import datetime

def extract_date_from_filename(filename):
    # Extract date from the filename, assuming the date is in the format YYMMDD
    try:
        date_str = filename[3:9]
        date_obj = datetime.strptime(date_str, '%y%m%d')
        return date_obj.strftime('%Y-%m-%d')
    except Exception as e:
        print(f"Error extracting date from filename {filename}: {e}")
        return None

def check_existing_files(destination_folder, filename_prefix):
    # Check if any file with the same first three letters exists in the destination folder
    for existing_filename in os.listdir(destination_folder):
        if existing_filename.startswith(filename_prefix):
            return True
    return False

def copy_files(source_folders, destination_folder, conditions):
    # Iterate through each source folder and its condition
    for folder, condition in zip(source_folders, conditions):
        # Check if the source folder exists
        if not os.path.exists(folder):
            print(f"Source folder {folder} does not exist.")
            continue

        # Iterate through all files in the source folder
        for filename in os.listdir(folder):
            source_path = os.path.join(folder, filename)
            
            # Check if the path is a file (not a directory)
            if os.path.isfile(source_path) and condition(filename):
                # Extract date from the filename
                date_folder_name = extract_date_from_filename(filename)
                if date_folder_name:
                    dated_destination_folder = os.path.join(destination_folder, date_folder_name)
                    
                    # Ensure the destination date folder exists
                    if not os.path.exists(dated_destination_folder):
                        os.makedirs(dated_destination_folder)
                        print(f"Created folder {dated_destination_folder}")
                    
                    # Check if a file with the same first three letters exists in the destination
                    filename_prefix = filename[:3]
                    if check_existing_files(dated_destination_folder, filename_prefix):
                        print(f"A file with prefix {filename_prefix} already exists in {dated_destination_folder}. Skipping {filename}.")
                        continue
                    
                    destination_path = os.path.join(dated_destination_folder, filename)
                    
                    # Copy the file to the destination folder
                    shutil.copy2(source_path, destination_path)
                    print(f"Copied {source_path} to {destination_path}")

# List of source folders
source_folders = [
    r'G:\My Drive\AUS races\a-Vn TRIALS',
    r'G:\My Drive\AUS races\Hong Kong Meetings',
    r'G:\My Drive\AUS races\Combined Meetings',
    r'G:\.shortcut-targets-by-id\0B-jX__SJo8V6Smt4SEFXZnkwcnc\NZ',
    r'G:\My Drive\AUS races'
]

# List of conditions for each folder
conditions = [
    lambda filename: filename.endswith('T'),       # Only files ending with 'T'
    lambda filename: filename.endswith('.mov'),    # Only .mov files
    lambda filename: filename.endswith('.zip'),    # Only .zip files
    lambda filename: filename.endswith('.mov'),    # Only .mov files
    lambda filename: filename.endswith('.mov')     # Only .mov files
]

# Destination folder
destination_folder = r'D:\Widget1\Widget\Videos\2024'

# Call the function to copy files
copy_files(source_folders, destination_folder, conditions)
