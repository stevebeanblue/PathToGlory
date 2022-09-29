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


class TheVault(models.Model):
    Roster_Id = models.IntegerField(default=0)
    Triumph = models.TextField()


class BonusArtifactsOfPower(models.Model):
    Name = models.TextField()
    Roster_Id = models.IntegerField(default=0)
    Vault_Id = models.ForeignKey(TheVault, related_name='BonusArtifactsOfPower',
                                 on_delete=models.CASCADE, default=0)


class BonusUniqueEnhancements(models.Model):
    Name = models.TextField()
    Roster_Id = models.IntegerField(default=0)
    Vault_Id = models.ForeignKey(TheVault, related_name='BonusUniqueEnhancements', on_delete=models.CASCADE, default=0)


class BonusSpells(models.Model):
    Name = models.TextField()
    Roster_Id = models.IntegerField(default=0)
    Vault_Id = models.ForeignKey(TheVault, related_name='BonusSpells', on_delete=models.CASCADE, default=0)


class BonusPrayers(models.Model):
    Name = models.TextField()
    Roster_Id = models.IntegerField(default=0)
    Vault_Id = models.ForeignKey(TheVault, related_name='BonusPrayers', on_delete=models.CASCADE, default=0)


class EndlessSpellsAndInvocations(models.Model):
    Name = models.TextField()
    Roster_Id = models.IntegerField(default=0)
    Vault_Id = models.ForeignKey(TheVault, related_name='EndlessSpellsAndInvocations', on_delete=models.CASCADE,
                                 default=0)


class Battalions(models.Model):
    Name = models.TextField()
    Roster_Id = models.IntegerField(default=0)
    Vault_Id = models.ForeignKey(TheVault, related_name='Battalions', on_delete=models.CASCADE, default=0)


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


class OrderOfBattle(models.Model):
    Roster_id = models.IntegerField(default=0)
    TotalUnits = models.IntegerField(default=0)
    Heroes = models.IntegerField(default=0)
    Monsters = models.IntegerField(default=0)
    WarMachines = models.IntegerField(default=0)
    Wizards = models.IntegerField(default=0)
    Priests = models.IntegerField(default=0)
    ReinforcedUnits = models.IntegerField(default=0)
    Allies = models.IntegerField(default=0)


class HeroDetails(models.Model):
    Name = models.TextField()
    Warscroll = models.TextField()
    CommandTrait = models.TextField()
    CoreEnhancement_Notes = models.TextField()
    Injury = models.BooleanField(default=False)
    RenownPoints = models.IntegerField(default=0)
    Points = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Warlord(HeroDetails):
    OrderOfBattle = models.ForeignKey(OrderOfBattle, related_name='Warlord', on_delete=models.CASCADE, default=0)


class Hero(HeroDetails):
    OrderOfBattle = models.ForeignKey(OrderOfBattle, related_name='Hero', on_delete=models.CASCADE, default=0)


class Unit(models.Model):
    OrderOfBattle = models.ForeignKey(OrderOfBattle, related_name='Unit', on_delete=models.CASCADE, default=0)
    Name = models.TextField()
    Warscroll = models.TextField()
    VeteranAbilities_Notes = models.TextField()
    Reinforced1 = models.BooleanField(default=False)
    Reinforced2 = models.BooleanField(default=False)
    CasualtyScore = models.IntegerField(default=0)
    RenownPoints = models.IntegerField(default=0)
    Points = models.IntegerField(default=0)
