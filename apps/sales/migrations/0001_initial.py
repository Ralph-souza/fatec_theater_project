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
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies_title', to='movies.moviesmodel')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies_price', to='movies.roomsmodel')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms_name', to='movies.roomsmodel')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Sales',
                'ordering': ['-created_at'],
            },
        ),
    ]
