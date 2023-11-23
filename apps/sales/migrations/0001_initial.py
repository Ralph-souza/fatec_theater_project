from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [("movies", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="SalesModel",
            fields=[
                (
                    "id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                (
                    "price",
                    models.FloatField(
                        choices=[(15, "R$15.50"), (25, "R$25.50"), (35, "R$35.50")],
                        default=15.5,
                    ),
                ),
                (
                    "seat",
                    models.IntegerField(
                        choices=[
                            (1, "Seat 1"),
                            (2, "Seat 2"),
                            (3, "Seat 3"),
                            (4, "Seat 4"),
                            (5, "Seat 5"),
                            (6, "Seat 6"),
                            (7, "Seat 7"),
                            (8, "Seat 8"),
                            (9, "Seat 9"),
                            (10, "Seat 10"),
                            (11, "Seat 11"),
                            (12, "Seat 12"),
                            (13, "Seat 13"),
                            (14, "Seat 14"),
                            (15, "Seat 15"),
                            (16, "Seat 16"),
                            (17, "Seat 17"),
                            (18, "Seat 18"),
                            (19, "Seat 19"),
                            (20, "Seat 20"),
                        ]
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="movie_sales",
                        to="movies.moviesmodel",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="room_sales",
                        to="movies.roomsmodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Sale",
                "verbose_name_plural": "Sales",
                "ordering": ["-created_at"],
            },
        )
    ]
