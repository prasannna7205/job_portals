# Generated by Django 4.2.1 on 2023-09-23 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyJobApp', '0003_job'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Job',
            new_name='JobTable',
        ),
    ]
