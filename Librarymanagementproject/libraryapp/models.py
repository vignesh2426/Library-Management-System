from django.db import models


# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.course_name}'

class Books(models.Model):
    Book_name=models.CharField(max_length=50)
    Author_name=models.CharField(max_length=50)
    Course_id=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Book_name}'

class Student(models.Model):
    Student_name=models.CharField(max_length=50)
    Student_password=models.CharField(max_length=50)
    Student_phno=models.BigIntegerField(default=0)
    Student_Sem=models.IntegerField(default=0)
    Student_course=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Student_name}'
class Issue_Book(models.Model):
    Student_Name=models.ForeignKey(Student,on_delete=models.CASCADE)
    Book_Name=models.ForeignKey(Books,on_delete=models.CASCADE)
    Start_date=models.DateField()
    End_date=models.DateField()
