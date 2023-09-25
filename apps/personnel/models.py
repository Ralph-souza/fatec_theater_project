from django.db import models

from apps.personnel.choices import RoleChoices


class ManagerModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.ForeignKey("account.Account", related_name="manager_email", on_delete=models.CASCADE)
    role = models.CharField(
        choices=RoleChoices.choices,
        max_length=20,
        default=RoleChoices.MANAGER,
        blank=False,
        null=False
    )
    is_admin = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")

    class Meta:
        verbose_name = 'Manager Permission'
        verbose_name_plural = 'Managers'
        ordering = ['id']

    def __str__(self):
        return self.name


class StaffModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.ForeignKey("account.Account", related_name="staff_email", on_delete=models.CASCADE)
    role = models.CharField(
        choices=RoleChoices.choices,
        max_length=20,
        default=RoleChoices.STAFF,
        blank=False,
        null=False
    )
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")

    class Meta:
        verbose_name = 'Staff Permission'
        verbose_name_plural = 'Employees'
        ordering = ['id']

    def __str__(self):
        return self.name

