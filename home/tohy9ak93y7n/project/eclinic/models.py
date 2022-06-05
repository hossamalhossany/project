from django.db import models


# Create your models here.


class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Patient_data(models.Model):
    patient_name = models.CharField(max_length=50)
    patient_sex = models.CharField(max_length=10)
    patient_address = models.CharField(max_length=30)

    def __str__(self):
        return self.patient_name


class registration_info(models.Model):
    registration_date = models.CharField(max_length=20)
    registration_type = models.CharField(max_length=20)

    def __str__(self):
        return self.registration_date
