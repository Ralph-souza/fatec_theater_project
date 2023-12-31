from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="StaffModel",
            fields=[
                (
                    "id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "role",
                    models.CharField(
                        choices=[("manager", "Manager"), ("staff", "Staff")],
                        default="staff",
                        max_length=20,
                    ),
                ),
                ("is_admin", models.BooleanField(default=False)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                (
                    "email",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="staff_email",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Staff Permission",
                "verbose_name_plural": "Employees",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="ManagerModel",
            fields=[
                (
                    "id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "role",
                    models.CharField(
                        choices=[("manager", "Manager"), ("staff", "Staff")],
                        default="manager",
                        max_length=20,
                    ),
                ),
                ("is_admin", models.BooleanField(default=True)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                (
                    "email",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="manager_email",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Manager Permission",
                "verbose_name_plural": "Managers",
                "ordering": ["id"],
            },
        ),
    ]
