# Generated by Django 3.2 on 2022-06-07 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BattlesFought', models.IntegerField()),
                ('QuestCompleted', models.IntegerField()),
                ('VictoriesWon', models.IntegerField()),
                ('EnemyHereosSlain', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Battalions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BonusArtifactsOfPower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BonusPrayers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BonusSpells',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BonusUniqueEnhancements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EndlessSpellsAndInvocations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ImposingStrongHoldTerritories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('TerritoryType', models.TextField()),
                ('Upgraded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MightyStrongholdTerritories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('TerritoryType', models.TextField()),
                ('Upgraded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PathToGloryGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='questlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CurrentQuest', models.TextField()),
                ('QuestReward', models.TextField()),
                ('QuestProgress', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Stronghold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Barracks', models.TextField()),
                ('Imposing', models.BooleanField(default=False)),
                ('Mighty', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StrongholdTerritories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('TerritoryType', models.TextField()),
                ('Upgraded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TheVault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Triumph', models.TextField()),
                ('Battalions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pathtoglory.battalions')),
                ('BonusArtifactsOfPower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pathtoglory.bonusartifactsofpower')),
                ('BonusPrayers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pathtoglory.bonusprayers')),
                ('BonusSpells', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pathtoglory.bonusspells')),
                ('BonusUniqueEnhancements', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pathtoglory.bonusuniqueenhancements')),
                ('EndlessSpellsAndInvocations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pathtoglory.endlessspellsandinvocations')),
            ],
        ),
        migrations.CreateModel(
            name='Territories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ImposingStrongHoldTerritories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pathtoglory.imposingstrongholdterritories')),
                ('MightyStrongholdTerritories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pathtoglory.mightystrongholdterritories')),
                ('StrongholdTerritories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pathtoglory.strongholdterritories')),
            ],
        ),
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlayerName', models.TextField()),
                ('Faction', models.TextField()),
                ('RealmOfOrigin', models.TextField()),
                ('ArmyName', models.TextField()),
                ('Subfaction', models.TextField()),
                ('StartingSize', models.IntegerField()),
                ('IsCompleted', models.BooleanField(default=False)),
                ('DateCreated', models.DateField()),
                ('Glory', models.IntegerField(default=0)),
                ('Achievements', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pathtoglory.achievements')),
                ('Group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pathtoglory.pathtoglorygroup')),
                ('questlog', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pathtoglory.questlog')),
                ('Stronghold', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pathtoglory.stronghold')),
                ('Territories', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pathtoglory.territories')),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Vault', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pathtoglory.thevault')),
            ],
        ),
    ]
