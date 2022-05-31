from django.db import models


# Create your models here.
class PathToGloryGroup(models.Model):
    Description = models.TextField()

    def __str__(self):
        return self.Description

class Rosters(models.Model):
    Group_id = reporter = models.ForeignKey(PathToGloryGroup, on_delete=models.CASCADE)
    PlayerName = models.TextField()
    Faction = models.TextField()
    RealmOfOrigin = models.TextField()
    ArmyName = models.TextField()
    Subfaction = models.TextField()
    StartingSize = models.IntegerField
