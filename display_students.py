from main import Student

students = Student.select()

for Student in students:
    print(Student.stud_name, Student.stud_email, Student.stud_password)




