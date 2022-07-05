from django import forms
from django.forms import ModelForm
from pathtoglory.models import Roster, QuestLog


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


# need to create editRosterForm with completed field or just remove from above

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
