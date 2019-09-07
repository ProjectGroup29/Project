from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('M','Male'),
    ('F','Female'),
    ('O','Others'),
)

class Profile(models.Model):
    name = models.CharField(max_length= 20)
    bio = models.TextField ()
    email = models.EmailField ()
    dob = models.DateField
    phone = models.CharField (max_length= 10)
    gender = models.CharField(max_length= 1 , choices= GENDER_CHOICES)
    address = models.TextField()
    acc_created = models.DateTimeField()
    def __str__(self):
        return self.name