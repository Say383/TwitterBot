import os
import subprocess
from datetime import datetime

class BackupManager:
    def __init__(self, db_uri, backup_dir='backups/'):
        self.db_uri = db_uri
        self.backup_dir = backup_dir

    def perform_backup(self):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        backup_file = os.path.join(self.backup_dir, f'db_backup_{timestamp}.sql')
        command = f'mysqldump -u user -ppassword {self.db_uri} > {backup_file}'
        subprocess.run(command, shell=True)
        print(f'Backup performed and saved to {backup_file}')

    def schedule_backup(self, cron_expression):
        # Placeholder for scheduling backups using cron or similar methods
        # Implement your scheduling logic here
        pass

    def list_backups(self):
        # List the available backups in the backup directory
        backup_files = os.listdir(self.backup_dir)
        return backup_files

    def delete_backup(self, backup_filename):
        # Delete a specific backup file
        backup_path = os.path.join(self.backup_dir, backup_filename)
        if os.path.exists(backup_path):
            os.remove(backup_path)
            print(f'{backup_filename} has been deleted.')
        else:
            print(f'{backup_filename} does not exist.')

# Example usage:
if __name__ == '__main__':
    db_uri = 'your_database_uri_here'  # Replace with your actual database URI
    backup_manager = BackupManager(db_uri)
    backup_manager.perform_backup()
    # List available backups
    backups = backup_manager.list_backups()
    print('Available Backups:')
    for backup in backups:
        print(backup)
    # Delete a specific backup (replace with an actual backup filename)
    # backup_manager.delete_backup('db_backup_20220120123456.sql')
# Call the function to perform backup
perform_backup('my_database_uri')



    # Additional methods for scheduling and managing backups can be added here
