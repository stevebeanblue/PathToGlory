from django import forms
from django.forms import ModelForm
from pathtoglory.models import Roster, QuestLog, Stronghold, Achievements, BonusArtifactsOfPower, \
    BonusUniqueEnhancements, BonusSpells, BonusPrayers, EndlessSpellsAndInvocations, Battalions, TheVault, \
    Warlord, OrderOfBattle, Hero, Unit


# region roster
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


# endregion
# region quest
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


# endregion
# region stronghold
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


# endregion
# region achievement
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


# endregion
# region BAoP
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


# endregion
# region BUE
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


# endregion
# region spell
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


# endregion
# region payers
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


# endregion
# region endless spell
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


# endregion
# region battalions
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


# endregion
# region vault
class TheVaultForm(ModelForm):
    class Meta:
        model = TheVault
        fields = {
            'Roster_Id',
            'Triumph'
        }
        widgets = {
            'Roster_Id': forms.HiddenInput(),
        }


# endregion
# region order of battle
class OrderOfBattleForm(ModelForm):
    class Meta:
        model = OrderOfBattle
        fields = {
            'Roster_id',
            'TotalUnits',
            'Heroes',
            'Monsters',
            'WarMachines',
            'Wizards',
            'Priests',
            'ReinforcedUnits',
            'Allies'
        }
        widgets = {
            'Roster_id': forms.HiddenInput()
        }


# endregion
# region warlord
class WarlordForm(ModelForm):
    class Meta:
        model = Warlord
        fields = {
            'OrderOfBattle',
            'Name',
            'Warscroll',
            'CommandTrait',
            'CoreEnhancement_Notes',
            'Injury',
            'RenownPoints',
            'Points'
        }
        widgets = {
            'OrderOfBattle': forms.HiddenInput()
        }


# endregion
# region Hero
class HeroForm(ModelForm):
    class Meta:
        model = Hero
        fields = {
            'OrderOfBattle',
            'Name',
            'Warscroll',
            'CommandTrait',
            'CoreEnhancement_Notes',
            'Injury',
            'RenownPoints',
            'Points'
        }
        widgets = {
            'OrderOfBattle': forms.HiddenInput()
        }


# endregion
# region unit
class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = {
            'OrderOfBattle',
            'Name',
            'Warscroll',
            'VeteranAbilities_Notes',
            'Reinforced1',
            'Reinforced2',
            'CasualtyScore',
            'RenownPoints',
            'Points'
        }
        widgets = {
            'OrderOfBattle': forms.HiddenInput()
        }
# end region
