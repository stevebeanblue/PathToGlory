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

class Roster(models.Model):
    Group_id = models.ForeignKey(
        PathToGloryGroup,
        on_delete=models.CASCADE)
    PlayerName = models.TextField()
    Faction = models.TextField()
    RealmOfOrigin = models.TextField()
    ArmyName = models.TextField()
    Subfaction = models.TextField()
    StartingSize = models.IntegerField()
    User = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    IsCompleted = models.BooleanField(default=False)
    DateCreated = models.DateField()
    Glory = models.IntegerField(default=0)
    QuestLog = models.OneToOneField(
        QuestLog,
        on_delete=models.CASCADE,
        default=QuestLog.objects.create
    )
