from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
import uuid
# Create your models here.


def image_directory_path(instance, filename):
    new_count = User.objects.latest('id').id + 1
    return f"users/{new_count}/{filename}"


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Users must have an email address.")
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.TextField()
    phone_number = models.CharField(max_length=50, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(verbose_name='profile picture',
                                        upload_to=image_directory_path,
                                        default='users/default.png',
                                        null=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    def __str__(self):
        return self.full_name

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['full_name', 'phone_number', 'date_of_birth', 'profile_picture']