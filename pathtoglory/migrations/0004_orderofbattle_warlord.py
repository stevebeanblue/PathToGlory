# Generated by Django 4.0.4 on 2022-09-08 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pathtoglory', '0003_auto_20220806_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderOfBattle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roster_id', models.IntegerField(default=0)),
                ('TotalUnits', models.IntegerField(default=0)),
                ('Heroes', models.IntegerField(default=0)),
                ('Monsters', models.IntegerField(default=0)),
                ('WarMachines', models.IntegerField(default=0)),
                ('Wizards', models.IntegerField(default=0)),
                ('Priests', models.IntegerField(default=0)),
                ('ReinforcedUnits', models.IntegerField(default=0)),
                ('Allies', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Warlord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Warscroll', models.TextField()),
                ('CommandTrait', models.TextField()),
                ('CoreEnhancement_Notes', models.TextField()),
                ('Injury', models.BooleanField(default=False)),
                ('RenownPoints', models.IntegerField(default=0)),
                ('Points', models.IntegerField(default=0)),
                ('OrderOfBattle', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Warlord', to='pathtoglory.orderofbattle')),
            ],
        ),
    ]
