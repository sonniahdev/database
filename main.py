from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Soniah.db"))


# creating our first table

class Student(Model):
    stud_name = CharField()
    stud_email = CharField()
    stud_password = CharField()

    class Meta:
        database = db


Student.create_table(fail_silently=True)


class Product(Model):
    prod_price = CharField()
    prod_quantity = CharField()
    prod_colour = CharField()

    class Meta:
        database = db


Product.create_table(fail_silently=True)


