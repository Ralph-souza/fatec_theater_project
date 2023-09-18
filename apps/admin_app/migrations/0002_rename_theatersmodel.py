from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller_app', '0002_rename_teather_ticketsmodel_theater'),
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TeathersModel',
            new_name='TheatersModel',
        ),
    ]
