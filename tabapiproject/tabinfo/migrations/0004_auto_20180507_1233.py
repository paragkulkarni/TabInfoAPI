# Generated by Django 2.0.4 on 2018-05-07 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabinfo', '0003_auto_20180507_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tabinfo',
            old_name='tabname',
            new_name='tab_name',
        ),
    ]
