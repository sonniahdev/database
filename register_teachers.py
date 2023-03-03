from main import Teacher

try:
    Teacher_name = input("Enter name \n")
    Teacher_phone = input("Enter phone \n")
    Teacher_email = input("Enter email \n")
    Teacher_password = input("Enter password")
    Teacher.create(tec_name=Teacher_name, tec_phone=Teacher_phone, tec_email=Teacher_email, tec_password=Teacher_password )
    print("Student Created Successfully")

except:
    print("Failed to Create Student")
