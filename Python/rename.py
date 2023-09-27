import os

folder_path = '//Users//albachocron//Library//CloudStorage//OneDrive-UniversityofTexasatSanAntonio//Epics'
new_prefix = 'image'
extension = '.jpg'  # Change this to match your image format

# List all files in the folder
file_list = os.listdir(folder_path)

# Sort the files to ensure sequential renaming
file_list.sort()

# Counter for the new filenames
counter = 1

for old_name in file_list:
    if old_name.endswith(extension):
        new_name = f"{new_prefix}_{counter:03d}{extension}"
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        
        print(f"Renamed: {old_name} -> {new_name}")
        
        counter += 1

print("Renaming complete.")

