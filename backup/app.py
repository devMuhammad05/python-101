import os
import shutil
import datetime
import schedule
import time

source_dir = r"C:\Users\X P S\Pictures\Screenshots"
destination_dir = r"C:\Users\X P S\Desktop\Backups"

def copy_folder_to_directory(source, destination):
    today = datetime.date.today()
    destination_dir = os.path.join(destination, str(today))

    try:
        shutil.copytree(source, destination_dir)
        print(f"Folder copied to: {destination_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {destination}")


# Schedule the backup to run every day
# schedule.every().day.at("06:00").do(copy_folder_to_directory, source_dir, destination_dir)

schedule.every().day.at("06:00").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

# Keep the scheduler running
while True:
    schedule.run_pending()
    time.sleep(10)