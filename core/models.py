
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
    )
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
# Create your models here.


class UserManager(BaseUserManager):
    """ Creating user handler """
    def create_user(
                    self, email, username,
                    first_name, last_name,
                    password=None,
                   ):

        if not email:
            raise ValueError('Please fill up email')
        if not username:
            raise ValueError('Please fill up the username')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
            )
        user.slug = slugify(user.username)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
                         self, email,
                         username, first_name,
                         last_name, password
                        ):

        user = self.create_user(
            email,
            username,
            first_name,
            last_name,
            password
            )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.is_admin = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Custome user model """

    username = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=36)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    """ Custom profile for users """
    full_name = models.CharField(max_length=256)
    slug = models.SlugField()
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
        )
    image = models.ImageField(
        default='profile_pics/gg.png',
        upload_to='profile_pics/'
        )
    bio = models.CharField(
        max_length=256,
        default='Tell us who you are.'
        )
    cover = models.ImageField(
        default='profile_cover/coverdefault.jpg',
        upload_to='profile_cover/'
        )

    def save(self, *args, **kwargs):
        self.full_name = f'{self.user.first_name} {self.user.last_name}'
        self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("page:profile_view", kwargs={"slug": self.slug})

    def __str__(self):
        return f'{self.user.username} Profile'


@receiver(user_signed_up)
def after_user_signed_up(sender, request, user, **kwargs):
    g = Profile.objects.create(user=user)
    g.save()
