import os
import zipfile
import shutil

def unzip_and_cleanup(zip_path, dest_dir):
    # Unzip the file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Get the list of file names in the zip file
        file_names = zip_ref.namelist()
        
        # Extract all files to the destination directory, excluding __MACOSX
        for file_name in file_names:
            if not file_name.startswith('__MACOSX/'):
                zip_ref.extract(file_name, dest_dir)
    
    # Check if files were unzipped into a subfolder
    subfolders = [f for f in os.listdir(dest_dir) if os.path.isdir(os.path.join(dest_dir, f))]
    
    if len(subfolders) == 1:
        subfolder_path = os.path.join(dest_dir, subfolders[0])
        
        # Move files from subfolder to parent directory
        for item in os.listdir(subfolder_path):
            shutil.move(os.path.join(subfolder_path, item), dest_dir)
        
        # Remove the now empty subfolder
        os.rmdir(subfolder_path)
    
    # Remove the zip file
    os.remove(zip_path)

def unzip_files_in_directory(directory):
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".zip"):
                # Full path of the zip file
                zip_path = os.path.join(root, file)
                print(f"Unzipping {zip_path}")
                
                # Unzip and cleanup
                unzip_and_cleanup(zip_path, root)

# Directory to search for zip files
base_directory = r'D:\Widget1\Widget\Videos\2024'

# Call the function
unzip_files_in_directory(base_directory)
