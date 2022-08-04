from django.conf import settings
from django.db import models


class PathToGloryGroup(models.Model):
    Description = models.TextField()

    def __str__(self):
        return self.Description


class QuestLog(models.Model):
    RosterId = models.IntegerField(default=0)
    CurrentQuest = models.TextField()
    QuestReward = models.TextField()
    QuestProgress = models.TextField()


class Stronghold(models.Model):
    RosterId = models.IntegerField(default=0)
    Name = models.TextField()
    Barracks = models.TextField()
    Imposing = models.BooleanField(default=False)
    Mighty = models.BooleanField(default=False)


class BonusArtifactsOfPower(models.Model):
    Name = models.TextField()
    Roster_Id = models.IntegerField(default=0)


class BonusUniqueEnhancements(models.Model):
    Name = models.TextField()
    Roster_Id = models.IntegerField(default=0)


class BonusSpells(models.Model):
    Name = models.TextField()
    Roster_Id = models.IntegerField(default=0)


class BonusPrayers(models.Model):
    Name = models.TextField()
    Roster_Id = models.IntegerField(default=0)


class EndlessSpellsAndInvocations(models.Model):
    Name = models.TextField()
    Roster_Id = models.IntegerField(default=0)


class Battalions(models.Model):
    Name = models.TextField()
    Roster_Id = models.IntegerField(default=0)


class TheVault(models.Model):
    Roster_Id = models.IntegerField(default=0)
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
    TerritoriesId = models.IntegerField(default=0)
    Name = models.TextField()
    TerritoryType = models.TextField()
    Upgraded = models.BooleanField(default=False)


class ImposingStrongHoldTerritories(models.Model):
    TerritoriesId = models.IntegerField(default=0)
    Name = models.TextField()
    TerritoryType = models.TextField()
    Upgraded = models.BooleanField(default=False)


class MightyStrongholdTerritories(models.Model):
    TerritoriesId = models.IntegerField(default=0)
    Name = models.TextField()
    TerritoryType = models.TextField()
    Upgraded = models.BooleanField(default=False)


class Roster(models.Model):
    Group_id = models.ForeignKey(
        PathToGloryGroup,
        on_delete=models.CASCADE
    )
    Group_id_as_int = models.IntegerField(default=0)
    PlayerName = models.TextField()
    Faction = models.TextField()
    RealmOfOrigin = models.TextField()
    ArmyName = models.TextField()
    Subfaction = models.TextField()
    StartingSize = models.IntegerField()
    User_id = models.IntegerField(default=0)
    Glory = models.IntegerField()
    Completed = models.BooleanField(default=False)
    DateCreated = models.DateField()


class Achievements(models.Model):
    RosterId = models.OneToOneField(Roster, on_delete=models.CASCADE, default=0)
    BattlesFought = models.IntegerField(default=0)
    QuestCompleted = models.IntegerField(default=0)
    VictoriesWon = models.IntegerField(default=0)
    EnemyHereosSlain = models.IntegerField(default=0)


class Territories(models.Model):
    RosterId = models.IntegerField(default=0)
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