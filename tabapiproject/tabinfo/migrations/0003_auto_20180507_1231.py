# Generated by Django 2.0.4 on 2018-05-07 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabinfo', '0002_auto_20180507_1222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tabinfo',
            old_name='sideeffect',
            new_name='side_effect',
        ),
    ]
