from django.forms import ModelForm
from pathtoglory.models import *

class CreateRosterForm(ModelForm):
    class Meta:
        model = Roster
        exclude = ("User", "DateCreated")

class QuestLogForm(ModelForm):
    class Meta:
        model = QuestLog
        exclude = ("RosterId",)


