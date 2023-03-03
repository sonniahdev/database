from main import Teacher

teachers = Teacher.select()

for Teacher in teachers:
    print(Teacher.tec_name, Teacher.tec_phone, Teacher.tec_email, Teacher.tec_password)

