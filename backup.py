import shutil
import os
import datetime

def backup(select_from, backup_to):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_folder = os.path.join(backup_to, f"backup_{timestamp}")

    try:
        # Create the backup folder
        os.makedirs(backup_folder)

        # Copy files and directories to the backup folder
        for selection in select_from:
            shutil.copytree(selection, os.path.join(backup_folder, os.path.basename(selection)))

        print("Backup completed successfully.")
    except Exception as e:
        print(f"Error during backup: {e}")

# Example usage:
select_from = ["D:\Programs\Python\CodesOnBytes", "D:\Programs\Python\Cognifyz"]
backup_to = "D:\Programs\Python\InternshipTasks"
backup(select_from, backup_to)