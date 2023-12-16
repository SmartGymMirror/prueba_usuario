from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Los usuarios deben tener un email')
        
        email=self.normalize_email(email) #el normalize_email nos permite poner el email en minusculas
        user=self.model(email=email, name=name)

        user.set_password(password) #set_password nos permite encriptar la contraseña
        user.save()

        return user
        

class UserAccount(AbstractBaseUser, PermissionsMixin, BaseUserManager):

    email=models.EmailField(max_length=255, unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserAccountManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']
    
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')


    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email


