# Generated by Django 3.1 on 2020-08-29 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='story',
            new_name='body',
        ),
    ]