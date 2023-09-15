from django.db import models


class AdminUserAuth(models.Model):
    username = models.CharField(max_length=50, unique=True, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField()

    class Meta:
        verbose_name = 'AdminUser'
        verbose_name_plural = 'AdminUsers'
        ordering = ['id']

    def __str__(self):
        return self.username


class SellerUserAuth(models.Model):
    username = models.CharField(max_length=50, unique=True, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'SellerUser'
        verbose_name_plural = 'SellerUsers'
        ordering = ['id']

    def __str__(self):
        return self.username
