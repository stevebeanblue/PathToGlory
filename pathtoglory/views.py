from django.shortcuts import render
from .models import PathToGloryGroup, Rosters


def home(request):
    if request.method == 'GET':
        return render(request, "home.html", {"PathToGloryGroup": list(PathToGloryGroup.objects.all())})

def groupRosters(request, group_id):
    if request.method == 'GET':
        return render(request, "groups/groupRosters.html", {"Rosters": list(Rosters.objects.filter(Group_id == group_id))})