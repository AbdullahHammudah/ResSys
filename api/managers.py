from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError(_("Users must have an email address."))


        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )

        user.is_admin = True
        user.is_staff = True 
        user.is_superuser = True
        user.save()
        return user 