from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models

## Extending the user model to make email the required field instead of the default 'username'
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

##New  User model
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255, unique=False)
    last_name = models.CharField(max_length=255, unique=False)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=80, unique=True, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'


    objects = UserManager()

    def __str__(self):
        return self.email


departments=[('ANES', 'Anesthetics'),
        ('CRDLGY','Cardiologist'),
        ('DMRTLGY','Dermatologists'),
        ('RAD','Radiology'),
        ('GYN', 'Gynecology')]


class Doctor(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    department = models.CharField(max_length=50, choices=departments, default='GYN')



    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)


class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    phone = models.CharField(max_length=20,null=False)
    date_admitted = models.DateField(auto_now=True)
    symptoms = models.CharField(max_length=100,null=False)
    assigned_to = models.OneToOneField(Doctor,on_delete=models.CASCADE)


    def __str__(self):
        return "%s %s" %( self.user.first_name, self.user.last_name)