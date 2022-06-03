from django.forms import ModelForm
from pathtoglory.models import Roster

class CreateRosterForm(ModelForm):
    class Meta:
        model = Roster
        exclude = ("User", "DateCreated")


