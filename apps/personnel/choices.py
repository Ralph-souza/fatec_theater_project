from django.db import models


class RoleChoices(models.TextChoices):
    """Available roles"""
    MANAGER = 'manager', 'Manager'
    STAFF = 'staff', 'Staff'
