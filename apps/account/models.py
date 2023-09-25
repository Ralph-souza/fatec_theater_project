from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an e-mail address!")
        if not username:
            raise ValueError("Users must have an username!")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True, verbose_name="email")
    username = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="date joined")
    last_login = models.DateTimeField(auto_now_add=True, verbose_name="last login")
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", ]

    objects = AccountManager()

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
        ordering = ["-date_joined"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
