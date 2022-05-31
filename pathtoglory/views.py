from django.shortcuts import render
from .models import PathToGloryGroup, Roster


def home(request):
    if request.method == 'GET':
        return render(request, "home.html", {"PathToGloryGroup": list(PathToGloryGroup.objects.all())})


def grouprosters(request, group_id):
    if request.method == 'GET':
        return render(request, "groups/groupRosters.html", {"Rosters": list(Roster.objects.filter(Group_id = group_id))})