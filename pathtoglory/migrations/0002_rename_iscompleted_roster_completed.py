# Generated by Django 3.2 on 2022-06-07 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pathtoglory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roster',
            old_name='IsCompleted',
            new_name='Completed',
        ),
    ]