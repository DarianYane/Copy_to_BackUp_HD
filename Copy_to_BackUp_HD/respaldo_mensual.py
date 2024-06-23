import shutil
import os
from datetime import datetime

# Configure paths
source_folders = {
    'C:\\Users\\daria\\Desktop': 'Desktop',
    'C:\\Users\\daria\\OneDrive': 'Onedrive'
}
base_destination_folder = 'D:\\'  # Cambia esta línea según la letra de tu disco externo

# Function to copy files and directories recursively
def backup_files():
    try:
        # Create the destination folder name with the current date
        today_date = datetime.now().strftime('%Y-%m-%d')
        destination_base_folder = os.path.join(base_destination_folder, today_date)

        # Check if the base destination folder exists, if not, create it
        if not os.path.exists(destination_base_folder):
            os.makedirs(destination_base_folder)

        # Copy files and directories from each source folder to the destination folder
        for source_folder, alias in source_folders.items():
            # Create subfolder name based on alias and date
            subfolder_name = f'{alias}_{today_date}'
            destination_folder = os.path.join(destination_base_folder, subfolder_name)

            # Check if the destination folder exists, if not, create it
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Copy files and directories from source to destination
            for item in os.listdir(source_folder):
                source_path = os.path.join(source_folder, item)
                destination_path = os.path.join(destination_folder, item)
                try:
                    if os.path.isdir(source_path):
                        # Use shutil.copytree to copy directories if not already existing
                        if not os.path.exists(destination_path):
                            shutil.copytree(source_path, destination_path)
                            print(f'Directory {item} successfully copied from {source_folder}.')
                        else:
                            print(f'Skipped copying {item} (directory already exists).')
                    elif os.path.isfile(source_path):
                        # Use shutil.copy2 to copy files
                        shutil.copy2(source_path, destination_path)
                        print(f'File {item} successfully copied from {source_folder}.')
                    else:
                        print(f'Skipped copying {item}.')
                except Exception as e:
                    print(f'Error copying {item}: {e}')

        print('Backup completed.')
    except Exception as e:
        print(f'Error during backup: {e}')

# Run the backup function
backup_files()
