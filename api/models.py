from random import choices
from tkinter import CASCADE
from django.db import models
from django.conf import settings

class StatusChoices(models.TextChoices):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    DELETED = 'deleted'

class Doctor(models.Model):
    name = models.CharField(max_length=256, blank=False)
    ssn = models.CharField(max_length=64, blank=False)
    status = models.CharField(max_length=16, choices=StatusChoices.choices, default= StatusChoices.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now= True, null=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='doctors')

class Clinic(models.Model):
    name = models.CharField(max_length=256, blank=False)
    ssn = models.CharField(max_length=64, blank=False)
    status = models.CharField(max_length=16, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='clinics')

class Contact(models.Model):
    key = models.CharField(max_length=256)
    value = models.CharField(max_length=256)
    status = models.CharField(max_length=16, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='contacts')

class Speciality (models.Model):
    name = models.CharField(max_length=256, null=False)
    description = models.CharField(max_length=256)
    parent = models.ForeignKey('self')
    status = models.CharField(max_length=16, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

class DoctorSpecialities(models.Model):
    doctor = models.ForeignKey(Doctor)
    speciality = models.ForeignKey(Speciality)
    status = models.CharField(max_length=16, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
