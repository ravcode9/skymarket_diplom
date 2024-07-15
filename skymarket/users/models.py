from enum import Enum
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserRoles(Enum):
    USER = 'user'
    ADMIN = 'admin'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name,
                    phone, password=None, role=UserRoles.USER.value):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role=role
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name,
                         phone, password=None, role=UserRoles.ADMIN.value):
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            role=role
        )
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    first_name = models.CharField(max_length=30, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    phone = models.CharField(max_length=35, verbose_name='телефон',
                             blank=True, null=True)
    avatar = models.ImageField(upload_to='users/avatars/',
                               verbose_name='аватар',
                               blank=True, null=True)
    town = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='активность')
    role = models.CharField(max_length=10, choices=UserRoles.choices(),
                            verbose_name='роль', default=UserRoles.USER.value)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"
        ordering = ['email']

    objects = UserManager()

    @property
    def is_superuser(self):
        return self.role == UserRoles.ADMIN.value

    @property
    def is_staff(self):
        return self.role == UserRoles.ADMIN.value

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return self.email
