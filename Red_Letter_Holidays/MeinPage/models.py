from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

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
    """User model."""

    username = None
    first_name=None
    last_name=None
    name=models.CharField(max_length=30,blank=True)
    email = models.EmailField(_('email address'), unique=True)
    city=models.CharField(max_length=30, blank=True)
    profile_pic=models.ImageField(blank=True)
    phone=models.CharField(max_length=10)
    termsAccepted=models.BooleanField()
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class Token_data(models.Model):
    email=models.CharField(max_length=100)
    reset_token=models.CharField(max_length=6)
    time=models.TimeField(auto_now=True)
    #valid=models.BooleanField(default=False)
    user= models.ForeignKey(User, on_delete=models.CASCADE , related_name="books")


class Hotel(models.Model):
    hotel_name=models.CharField(max_length=255)
    hotel_address=models.CharField(max_length=255)
    room_type=models.CharField(max_length=255)
    inclusive=models.CharField(max_length=255)
    meal_type=models.CharField(max_length=255)
    amenities=models.CharField(max_length=255)
    price=models.CharField(max_length=255)
    image=models.ImageField()

class Package(models.Model):
    Cities=models.CharField(max_length=255)
    Country=models.CharField(max_length=255)
    Start_date=models.CharField(max_length=255)
    End_date=models.CharField(max_length=255)
    Flight_inbound=models.CharField(max_length=255)
    Flight_outbound=models.CharField(max_length=255)
    Flight_prise=models.CharField(max_length=255)
    Land_prise=models.CharField(max_length=255)
    Totel_prise=models.CharField(max_length=255)
    Hotels=models.ForeignKey(Hotel, on_delete=models.CASCADE)
    Meal_included=models.CharField(max_length=255)
    Activities_include=models.CharField(max_length=255)
    Visa_included=models.CharField(max_length=255)
    Meal_included=models.CharField(max_length=255)
    Acivities_included=models.CharField(max_length=255)
    Exclusive=models.CharField(max_length=255)
    Meal_included=models.CharField(max_length=255)
    Itnerary=models.TextField()
    Company_details=models.CharField(max_length=255)
    Transfer_detail=models.CharField(max_length=255)
    Freebies=models.CharField(max_length=255)
    Transfer_detail_seperate=models.CharField(max_length=255)
    seperate_sic_or_private=models.CharField(max_length=255)
    image=models.ImageField()

