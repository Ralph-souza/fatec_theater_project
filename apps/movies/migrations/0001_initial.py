from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('casting', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('horror', 'Horror'), ('comedy', 'Comedy'), ('drama', 'Drama'), ('thriller', 'Thriller')], max_length=50)),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Movie Name',
                'verbose_name_plural': 'Movies',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RoomsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('room', models.CharField(choices=[('room_1', 'Room 1'), ('room_2', 'Room 2'), ('room_3', 'Room 3')], max_length=100)),
                ('seats', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Available Room',
                'verbose_name_plural': 'Rooms',
                'ordering': ['id'],
            },
        ),
    ]
