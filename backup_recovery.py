import os
import shutil
from datetime import datetime
import schedule
import time
from threading import Thread

def backup_data():
    source_dir = 'data_directory'
    backup_dir = 'backup_directory'
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f'backup_{timestamp}')
    
    try:
        shutil.copytree(source_dir, backup_path)
        print(f"Backup created at {backup_path}")
    except Exception as e:
        print(f"Backup failed: {e}")

def schedule_backup():
    schedule.every().day.at("00:00").do(backup_data)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    schedule_backup()
    Thread(target=run_scheduler).start()
