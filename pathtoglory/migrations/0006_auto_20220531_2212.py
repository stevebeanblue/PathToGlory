# Generated by Django 3.2 on 2022-05-31 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathtoglory', '0005_rosters_iscompleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rosters',
            old_name='isCompleted',
            new_name='IsCompleted',
        ),
        migrations.AddField(
            model_name='rosters',
            name='StartingSize',
            field=models.IntegerField(default=False),
            preserve_default=False,
        ),
    ]
