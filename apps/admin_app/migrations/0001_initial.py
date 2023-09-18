from django.db import migrations, models
import django.db.models.deletion


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
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RoomsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(choices=[('room_1', 'Room 1'), ('room_2', 'Room 2'), ('room_3', 'Room 3')], max_length=100)),
                ('seats', models.IntegerField()),
                ('three_d', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TeathersModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.roomsmodel')),
                ('titles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.moviesmodel')),
            ],
            options={
                'verbose_name': 'Theater',
                'verbose_name_plural': 'Theaters',
                'ordering': ['id'],
            },
        ),
    ]
