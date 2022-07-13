from django import forms
from django.forms import ModelForm
from pathtoglory.models import Roster, QuestLog, Stronghold, Achievements


class CreateRosterForm(ModelForm):
    class Meta:
        model = Roster
        fields = {
            'Group_id',
            'PlayerName',
            'Faction',
            'RealmOfOrigin',
            'ArmyName',
            'Subfaction',
            'StartingSize',
            'User_id',
            'Glory',
            'Completed',
            'DateCreated'
        }
        widgets = {
            'PlayerName': forms.HiddenInput(),
            'User_id': forms.HiddenInput(),
            'DateCreated': forms.HiddenInput(),
            'Completed': forms.HiddenInput(),
        }


class QuestLogForm(ModelForm):
    class Meta:
        model = QuestLog
        fields = {
            'RosterId',
            'CurrentQuest',
            'QuestReward',
            'QuestProgress',
        }
        widgets = {
            'RosterId': forms.HiddenInput(),
        }


class StrongholdForm(ModelForm):
    class Meta:
        model = Stronghold
        fields = {
            'RosterId',
            'Name',
            'Barracks',
            'Imposing',
            'Mighty',
        }
        widgets = {
            'RosterId': forms.HiddenInput(),
        }

class AchievementsForm(ModelForm):
    class Meta:
        model = Achievements
        fields = {
            'RosterId',
            'BattlesFought',
            'QuestCompleted',
            'VictoriesWon',
            'EnemyHereosSlain',
        }
        widgets = {
            'RosterId': forms.HiddenInput(),
        }
