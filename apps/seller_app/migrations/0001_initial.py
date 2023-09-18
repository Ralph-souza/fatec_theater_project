from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.moviesmodel')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.roomsmodel')),
                ('teather', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.teathersmodel')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
                'ordering': ['-created_at'],
            },
        ),
    ]
