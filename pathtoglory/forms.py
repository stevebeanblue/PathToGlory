from django import forms
from django.forms import ModelForm
from pathtoglory.models import Roster, QuestLog, Stronghold, Achievements, BonusArtifactsOfPower, \
    BonusUniqueEnhancements, BonusSpells, BonusPrayers, EndlessSpellsAndInvocations, Battalions, TheVault


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
            'DateCreated',
            'Group_id_as_int',
        }
        widgets = {
            'PlayerName': forms.HiddenInput(),
            'User_id': forms.HiddenInput(),
            'DateCreated': forms.HiddenInput(),
            'Completed': forms.HiddenInput(),
            'Group_id_as_int': forms.HiddenInput(),
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


class BonusArtifactsOfPowerForm(ModelForm):
    class Meta:
        model = BonusArtifactsOfPower
        fields = {
            'Name',
            'Roster_Id',
            'Vault_Id',
        }
        widgets = {
            'Roster_Id': forms.HiddenInput(),
            'Vault_Id': forms.HiddenInput()
        }

class BonusUniqueEnhancementsForm(ModelForm):
    class Meta:
        model = BonusUniqueEnhancements
        fields = {
            'Name',
            'Roster_Id',
            'Vault_Id',
        }
        widgets = {
            'Roster_Id': forms.HiddenInput(),
            'Vault_Id': forms.HiddenInput()
        }

class BonusSpellsForm(ModelForm):
    class Meta:
        model = BonusSpells
        fields = {
            'Name',
            'Roster_Id',
            'Vault_Id',
        }
        widgets = {
            'Roster_Id': forms.HiddenInput(),
            'Vault_Id': forms.HiddenInput()
        }

class BonusPrayersForm(ModelForm):
    class Meta:
        model = BonusPrayers
        fields = {
            'Name',
            'Roster_Id',
            'Vault_Id',
        }
        widgets = {
            'Roster_Id': forms.HiddenInput(),
            'Vault_Id': forms.HiddenInput()
        }

class EndlessSpellsAndInvocationsForm(ModelForm):
    class Meta:
        model = EndlessSpellsAndInvocations
        fields = {
            'Name',
            'Roster_Id',
            'Vault_Id',
        }
        widgets = {
            'Roster_Id': forms.HiddenInput(),
            'Vault_Id': forms.HiddenInput()
        }

class BattalionsForm(ModelForm):
    class Meta:
        model = Battalions
        fields = {
            'Name',
            'Roster_Id',
            'Vault_Id',
        }
        widgets = {
            'Roster_Id': forms.HiddenInput(),
            'Vault_Id': forms.HiddenInput()
        }

class TheVaultForm(ModelForm):
    class Meta:
        model = TheVault
        fields = {
            'Roster_Id',
            'Triumph'
        }
        widgets = {
            'Roster_Id': forms.HiddenInput()
        }