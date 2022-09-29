# Generated by Django 4.0.4 on 2022-09-25 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pathtoglory', '0004_orderofbattle_warlord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Warscroll', models.TextField()),
                ('CommandTrait', models.TextField()),
                ('CoreEnhancement_Notes', models.TextField()),
                ('Injury', models.BooleanField(default=False)),
                ('RenownPoints', models.IntegerField(default=0)),
                ('Points', models.IntegerField(default=0)),
                ('OrderOfBattle', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Hero', to='pathtoglory.orderofbattle')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
