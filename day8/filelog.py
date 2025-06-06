import os
import datetime

class FilelogManager:
    def __init__(self, log_file="app_log.log"):
        self.log_file = log_file
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as file:
                file.write("==Log File Initialized==\n")

    def write_log(self, message, level="INFO"):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}][{level.upper()}] {message.strip()}\n"
        with open(self.log_file, 'a') as file:
            file.write(log_entry)
        print(f"log written: {log_entry}", end='')

    def read_logs(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as file:
                logs = file.read()
            print()
            print("==Log File Content==")
            print(logs)
        else:
            print("Log File doesn't exist.")

    def filter_logs(self, keyword):
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as file:
                logs = file.readlines()

            filtered_logs = []
            for log in logs:
                if keyword in log:
                    filtered_logs.append(log)

            print(f"==Logs Containing '{keyword}'==")
            if filtered_logs:
                for log in filtered_logs:
                    print(log, end='')
            else:
                print(f"No logs found containing '{keyword}'.")
        else:
            print("Log file doesn't exist.")

if __name__ == "__main__":
    log_manager = FilelogManager()
    log_manager.write_log("Application started.", level="INFO")
    log_manager.write_log("User logged in.", level="INFO")
    log_manager.write_log("An error occurred.", level="ERROR")

    log_manager.read_logs()
    log_manager.filter_logs("Error")
