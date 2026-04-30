def update_student_record(filename, name, subject, mode='a'):
    """
    mode='a' appends to the file (adds to existing data).
    mode='w' overwrites the file (starts fresh).
    """
    try:
        with open(filename, mode) as file:
            intro = f"Student Name: {name}, Favorite Subject: {subject}\n"
            file.write(intro)
        print(f"Successfully updated {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")


update_student_record("class_8_records.txt", "Roy", "Python", mode='w')

update_student_record("class_8_records.txt", "Ananya", "Mathematics", mode='a')
update_student_record("class_8_records.txt", "Arjun", "French", mode='a')