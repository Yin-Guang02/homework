total_working_days = int(input("Enter the total number of working days: "))
absent_days = int(input("Enter the total number of days absent: "))

attended_days = total_working_days - absent_days

attendance_percentage = (attended_days / total_working_days) * 100

print(f"\nYour attendance percentage is: {attendance_percentage:.2f}%")

if attendance_percentage < 75:
    print("Status: You are NOT eligible to sit in the exam.")
else:
    print("Status: You are eligible to sit in the exam.")