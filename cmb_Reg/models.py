# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class BioData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    birthday = models.DateField()
    nic = models.CharField(max_length=12)
    gender = models.CharField(max_length=12, choices=(('Male', 'Male'), ('Female', 'Female')))
    marital_status = models.CharField(max_length=12, choices=(('Single', 'Single'), ('Married', 'Married')))
    contact = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    scanned_nic = models.FileField()
    profile_pic = models.FileField()
    e_name = models.CharField(max_length=100, default='')
    e_relationship = models.CharField(max_length=100, default='')
    e_contact = models.CharField(max_length=12, default='')
    e_address = models.CharField(max_length=100, default='')

class Qualifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    al_year = models.CharField(max_length=100, default='')
    stream = models.CharField(max_length=100, default ="")
    subject1 = models.CharField(max_length=100)
    subject2 = models.CharField(max_length=100)
    subject3 = models.CharField(max_length=100)
    subject4 = models.CharField(max_length=100)
    result1 = models.CharField(max_length=1)
    result2 = models.CharField(max_length=1)
    result3 = models.CharField(max_length=1)
    result4 = models.CharField(max_length=1)
    resultSheet = models.FileField()
    degreeName = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    gpa = models.CharField(max_length=100)
    degreeClass = models.CharField(max_length=100)
    degreestartYear = models.CharField(max_length=5)
    graduateYear = models.CharField(max_length=5)
    transcript = models.FileField()

class Employment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    c_name = models.CharField(max_length=100)
    c_designation = models.CharField(max_length=100)
    c_duties = models.CharField(max_length=100)
    c_contact = models.CharField(max_length=100)
    c_email = models.CharField(max_length=100)
    c_fax = models.CharField(max_length=100)
    c_address = models.CharField(max_length=100)
    p_name = models.CharField(max_length=100)
    p_designation = models.CharField(max_length=100)
    p_duties = models.CharField(max_length=100)
    p_startDate = models.DateField()
    p_endDate = models.DateField()
    p_address = models.CharField(max_length=100)


class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    journal = models.CharField(max_length=100)
    doi = models.CharField(max_length=200, default='')
    abstract = models.CharField(max_length=200)
    title2 = models.CharField(max_length=100, default='')
    authors2 = models.CharField(max_length=100, default='')
    journal2 = models.CharField(max_length=100, default='')
    doi2 = models.CharField(max_length=200, default='')
    abstract2 = models.CharField(max_length=200, default="")

class refrees(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    r1_name = models.CharField(max_length=100)
    r1_designation = models.CharField(max_length=100)
    r1_organization = models.CharField(max_length=100)
    r1_contact = models.CharField(max_length=100)
    r1_address = models.CharField(max_length=100)
    r1_email = models.CharField(max_length=100,default="")
    r2_name = models.CharField(max_length=100)
    r2_designation = models.CharField(max_length=100)
    r2_organization = models.CharField(max_length=100)
    r2_contact = models.CharField(max_length=100)
    r2_address = models.CharField(max_length=100)
    r2_email = models.CharField(max_length=100, default="")

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=50)
    reference_number = models.CharField(max_length=50)
    applied_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.course_name}"