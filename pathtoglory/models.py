from django.conf import settings
from django.db import models

class PathToGloryGroup(models.Model):
    Description = models.TextField()

    def __str__(self):
        return self.Description

class QuestLog(models.Model):
    CurrentQuest = models.TextField()
    QuestReward = models.TextField()
    QuestProgress = models.TextField()

class Stronghold(models.Model):
    Name = models.TextField()
    Barracks = models.TextField()
    Imposing = models.BooleanField(default=False)
    Mighty = models.BooleanField(default=False)

class Achievements(models.Model):
    BattlesFought = models.IntegerField()
    QuestCompleted = models.IntegerField()
    VictoriesWon = models.IntegerField()
    EnemyHereosSlain = models.IntegerField()

class BonusArtifactsOfPower(models.Model):
    Name = models.TextField()

class BonusUniqueEnhancements(models.Model):
    Name = models.TextField()

class BonusSpells(models.Model):
    Name = models.TextField()

class BonusPrayers(models.Model):
    Name = models.TextField()

class EndlessSpellsAndInvocations(models.Model):
    Name = models.TextField()

class Battalions(models.Model):
    Name = models.TextField()

class TheVault(models.Model):
    Triumph = models.TextField()
    BonusArtifactsOfPower = models.ForeignKey(
        BonusArtifactsOfPower,
        on_delete=models.CASCADE
    )
    BonusUniqueEnhancements = models.ForeignKey(
        BonusUniqueEnhancements,
        on_delete=models.CASCADE
    )
    BonusSpells = models.ForeignKey(
        BonusSpells,
        on_delete=models.CASCADE
    )
    BonusPrayers = models.ForeignKey(
        BonusPrayers,
        on_delete=models.CASCADE
    )
    EndlessSpellsAndInvocations = models.ForeignKey(
        EndlessSpellsAndInvocations,
        on_delete=models.CASCADE
    )
    Battalions = models.ForeignKey(
        Battalions,
        on_delete=models.CASCADE
    )


class StrongholdTerritories(models.Model):
    Name = models.TextField()
    TerritoryType = models.TextField()
    Upgraded = models.BooleanField(default=False)

class ImposingStrongHoldTerritories(models.Model):
    Name = models.TextField()
    TerritoryType = models.TextField()
    Upgraded = models.BooleanField(default=False)

class MightyStrongholdTerritories(models.Model):
    Name = models.TextField()
    TerritoryType = models.TextField()
    Upgraded = models.BooleanField(default=False)

class Territories(models.Model):
    StrongholdTerritories = models.ForeignKey(
        StrongholdTerritories,
        on_delete=models.CASCADE
    )
    ImposingStrongHoldTerritories = models.ForeignKey(
        ImposingStrongHoldTerritories,
        on_delete=models.CASCADE
    )
    MightyStrongholdTerritories = models.ForeignKey(
        MightyStrongholdTerritories,
        on_delete=models.CASCADE
    )

class Roster(models.Model):
    Group_id = models.ForeignKey(
        PathToGloryGroup,
        on_delete=models.CASCADE
    )
    PlayerName = models.TextField()
    Faction = models.TextField()
    RealmOfOrigin = models.TextField()
    ArmyName = models.TextField()
    Subfaction = models.TextField()
    StartingSize = models.IntegerField()
    User = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    Completed = models.BooleanField(default=False)
    DateCreated = models.DateField()
    Glory = models.IntegerField(default=0)
    QuestLog = models.OneToOneField(
        QuestLog,
        on_delete=models.CASCADE,
    )
    Stronghold = models.OneToOneField(
        Stronghold,
        on_delete=models.CASCADE,
    )
    Achievements = models.OneToOneField(
        Achievements,
        on_delete=models.CASCADE,
    )
    Vault = models.OneToOneField(
        TheVault,
        on_delete=models.CASCADE,
    )
    Territories = models.OneToOneField(
        Territories,
        on_delete=models.CASCADE,
    )
