from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, Group
from django.db import models
from django.http import Http404
from django.utils.timezone import now


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password=password, )
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    date_joined = models.DateField(verbose_name='date joined', default=now().date)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    groups = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin


# Права доступа
def group_required(*group_names):
    def in_groups(user):
        if user.is_authenticated:
            if user.is_staff or (str(user.groups) in group_names):
                return True
        raise Http404
    return user_passes_test(in_groups)
