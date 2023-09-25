from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.moviesmodel')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.roomsmodel')),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.theatersmodel')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Sales',
                'ordering': ['-created_at'],
            },
        ),
    ]
