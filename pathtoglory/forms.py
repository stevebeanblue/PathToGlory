from django.forms import ModelForm
from pathtoglory.models import PathToGloryGroup, Rosters


class HomeForm(ModelForm):
    class Meta:
        model = PathToGloryGroup
        fields = '__all__'


class GroupRostersForm(ModelForm):
    class Meta:
        model = Rosters
        fields = '__all__'
