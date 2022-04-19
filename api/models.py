from api.managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class StatusChoices(models.TextChoices):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    DELETED = 'deleted'

class UserTypeChoices (models.TextChoices):
    PATIENT = 'Patient'
    CLINIC = 'Clinic'
    DOCTOR = 'Doctor'
    ADMIN = 'Admin'
    MODERATOR = 'Moderator'


class User (AbstractUser):
    # User's Personal Info
    email = models.EmailField(('email address'),max_length=60, unique=True)
    name = models.CharField(('first name'), max_length=150, blank=True)
    # User's authorizations Params
    type = models.CharField(max_length=16, choices=UserTypeChoices.choices, default= UserTypeChoices.NORMAL_USER)
    
    status = models.CharField(max_length=16, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'email',
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = 'users'
        verbose_name = ('user')
        verbose_name_plural = ('users')
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_name(self):
        """Return the name for the user."""
        return self.name
    
    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"

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

class Doctor(models.Model):
    name = models.CharField(max_length=256, blank=False)
    ssn = models.CharField(max_length=64, blank=False)
    status = models.CharField(max_length=16, choices=StatusChoices.choices, default= StatusChoices.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now= True, null=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='doctors')
    speciality = models.ManyToManyField('Speciality',through='DoctorSpecialities', related_name='doctors', )
class Speciality (models.Model):
    name = models.CharField(max_length=256, null=False)
    description = models.CharField(max_length=256)
    parent = models.ForeignKey('self', related_name='sub_speciality')
    status = models.CharField(max_length=16, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

class DoctorSpecialities(models.Model):
    doctor = models.ForeignKey('Doctor', related_name='doctor_specialities')
    speciality = models.ForeignKey('Speciality', related_query_name='doctor_specialities')
    status = models.CharField(max_length=16, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
