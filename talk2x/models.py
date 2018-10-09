from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
from .validators import *
from django.utils.text import slugify
from datetime import date

# Create your models here.



class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    #checks if email is a code email

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):

    email = models.EmailField(('email address'), unique=True, validators=[validate_code_mail])
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    picture = models.ImageField(upload_to='users/', blank=True, null=True)
    meaning_of_life = models.CharField(max_length=100, default='meaning of life')

    #only for is_staff
    DAY_CHOICES = (
        ('MONDAY', 'monday'),
        ('TUESDAY', 'tuesday'),
        ('WEDNESDAY', 'wednesday'),
        ('THURSDAY', 'thursday'),
        ('FRIDAY', 'friday'),
        ('EVERYDAY', 'everyday')
    )

    availabilty = models.CharField(max_length=10, choices=DAY_CHOICES, blank=True, null=True)
    subscribe_to_email = models.BooleanField(default = True)
    accepted_tc = models.BooleanField(default = False)

    slug =  models.SlugField(max_length = 30)

    def save(self, *args, **kwargs):
        if self.first_name == None:
            self.slug = slugify(self.first_name)
        else:
            slug = self.email.partition('@')[0]
            self.slug = slugify(slug)
        super(User, self).save(*args, **kwargs)

    objects = UserManager()

    def __str__(self):
        return self.email

    #code taken from https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    coupon = models.CharField(max_length=30,blank=True, null=True)
    street = models.CharField(max_length=20)
    no = models.PositiveSmallIntegerField()
    email = models.EmailField(blank=True, null=True)
    picture = models.ImageField(upload_to='restaurants/', blank=True, null=True)

    def __str__(self):
        return self.name

class Lunch(models.Model):
    date = models.DateField()
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE, null = True, blank = True)
    user = models.ManyToManyField(User)

    def __str__(self):

        ret_str = str(self.date)

        if not self.restaurant:
            return ret_str
        else:
            return self.restaurant.name + ' ' + ret_str

class FutureLunch(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateField(validators=[validate_lunch_date])
    is_active = models.BooleanField(default = True)

    def __str__(self):

        return self.user.email + ' ' + str(self.date)
