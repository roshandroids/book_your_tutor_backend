from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Commons(models.Model):
    status = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Tutor(Commons):
    TUTOR_GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),

    )

    reg_no = models.CharField(max_length=50,default='')
    name = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10,choices=TUTOR_GENDER,default='Others')
    city = models.CharField(max_length=50, default='')
    street = models.CharField(max_length=50, default='')
    contact = models.CharField(max_length=50, default='')
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class Customer(Commons):
    CUSTOMER_GENDER = (
        ('Male','Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),

    )

    name = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10,choices=CUSTOMER_GENDER,default='Others')
    city = models.CharField(max_length=50, default='')
    street = models.CharField(max_length=50, default='')
    contact = models.CharField(max_length=50, default='')
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Subject(Commons):
    SUBJECT_LEVEL = (
        ('Beginner','Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advance', 'Advance'),

    )
    name = models.CharField(max_length=100, default='')
    code = models.CharField(max_length=30,default='')
    address = models.CharField(max_length=100,default='')
    duration = models.IntegerField(default=0)
    level = models.CharField(max_length=20,choices=SUBJECT_LEVEL,default='Beginner')

    def __str__(self):
        return self.name

    

class TutorSubject(Commons):
    tutorId = models.ForeignKey(Tutor,on_delete=models.PROTECT)
    subjectId = models.ForeignKey(Subject,on_delete=models.PROTECT)
    price = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    # time=models.TimeField()
   
class TutorSubjectSchedule(Commons):
    tutorSubject = models.ForeignKey(TutorSubject,on_delete=models.PROTECT)
    date = models.DateField(default=timezone.now())
    time = models.TimeField(default=datetime.time(16, 00))

    def __str__(self):
        return self.name
    
    

class CustomerTutor(Commons):
    customerId = models.ForeignKey(Customer,on_delete=models.PROTECT)
    tutorSubject = models.ForeignKey(TutorSubject,on_delete=models.PROTECT)
    enrollmentDate = models.DateTimeField(default=timezone.now())
    Commons._meta.get_field('status').status = False

class Session(Commons):
    startDate = models.DateTimeField(default=timezone.now())
    endDate = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=2))
    subjectId = models.ForeignKey(Subject,on_delete=models.PROTECT)
    tutorId = models.ForeignKey(Tutor,on_delete=models.PROTECT)
    price = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)

class SessionCustomer(Commons):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    session = models.ForeignKey(Session, on_delete=models.PROTECT)
    Commons._meta.get_field('status').status = False


class TutorRating(Commons):
    tutorId = models.ForeignKey(Tutor,on_delete=models.PROTECT)
    customerId = models.ForeignKey(Customer,on_delete=models.PROTECT)
    rating = models.FloatField(default=10.0)

   

class Review(Commons):
    tutorId = models.ForeignKey(Tutor,on_delete=models.PROTECT)
    customerId = models.ForeignKey(Customer,on_delete=models.PROTECT)
    review = models.TextField(default="")

class Invoice(Commons):
    tutorCustomerId = models.ForeignKey(CustomerTutor,on_delete=models.PROTECT)
    amount = models.IntegerField(default=0)
    Commons._meta.get_field('status').status = False

class InvoiceSession(Commons):
    session = models.ForeignKey(Session,on_delete=models.PROTECT)
    amount = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    Commons._meta.get_field('status').status = False




