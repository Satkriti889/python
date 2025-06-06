import os
import datetime

class AttendanceManager:
    def __init__(self, attendance_file="staff_attendance.log"):
        self.attendance_file = attendance_file
        if not os.path.exists(self.attendance_file):
            with open(self.attendance_file, 'w') as file:
                file.write("== Staff Attendance Log Initialized ==\n")

    def log_attendance1(self, staff_name,level="Check IN" ):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] [{level.upper()}] {staff_name.strip()}\n"
        with open(self.attendance_file, 'a') as file:
            file.write(entry)
        print(f"Attendance {level} logged for {staff_name} at {timestamp}.")

    def log_attendance2(self,staff_name,level="Check OUT"):
        if os.path.exists(self.attendance_file):
            with open(self.attendance_file, 'r') as file:
                logs= file.read()
            print()
            print("\n== Staff Attendance Records ==")
            print(logs)
        else:
            print("Attendance file doesn't exist.")

    def filter_attendance(self, keyword):
        if os.path.exists(self.attendance_file):
            with open(self.attendance_file, 'r') as file:
                logs = file.readlines()

            filtered_logs = []
            for log in logs:
                if keyword in log:
                    filtered_logs.append(log)


            print(f"\n== Attendance Records Containing '{keyword}' ==")
            if filtered_logs:
                for log in filtered_logs:
                    print(log, end='')
            else:
                print(f"No attendance records found containing '{keyword}'.")
        else:
            print("Attendance file doesn't exist.")
    
    def view_attendance(self):
        if os.path.exists(self.attendance_file):
                with open(self.attendance_file, 'r') as file:
                    logs= file.read()
                print()
                print("\n== Staff Attendance Records ==")
                print(logs)
        else:
            print("Attendance doesn't exist..")

        

if __name__ == "__main__": 
    attendance = AttendanceManager()

    while True:
        print("\nStaff Attendance System Menu:")
        print("1. Check In")
        print("2. Check Out")
        print("3. Search Attendance")
        print("4. View Attendance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            name = input("Enter staff name to check in: ").strip()
            attendance.log_attendance1(name, "Check-In")
        elif choice=='2':
            name = input("Enter staff name to check out: ").strip()
            attendance.log_attendance2(name, "Check OUT")
        elif choice == '3':
            keyword = input("Enter keyword (name or date) to search attendance: ")
            attendance.filter_attendance(keyword)
        elif choice=='4':
            attendance.view_attendance()

        elif choice=='5':
            print("...Thank You...")
            break
        else:
            print("Invalid choice please enter the valid number between 1-4")