# Generated by Django 2.0.4 on 2018-05-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tabinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tabname', models.CharField(max_length=50)),
                ('ingredients', models.CharField(max_length=300)),
                ('unit_mg', models.IntegerField(max_length=3)),
                ('company', models.CharField(max_length=300)),
                ('uses', models.CharField(max_length=1000)),
                ('sideeffect', models.CharField(max_length=1000)),
            ],
        ),
    ]
