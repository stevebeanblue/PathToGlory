from django.shortcuts import render
from .models import PathToGloryGroup, Roster
from .forms import CreateRosterForm

def home(request):
    if request.method == 'GET':
        return render(request, "home.html", {"PathToGloryGroup": list(PathToGloryGroup.objects.all())})

def grouprosters(request, group_id):
    if request.method == 'GET':
        return render(request, "groups/groupRosters.html",
                      {"Rosters": list(Roster.objects.filter(Group_id = group_id))})

def createroster(request):
    if request.method == 'GET':
        return render(request, "rosters/create_roster.html", {"form": CreateRosterForm()})

def editroster(request, roster_id):
    roster = Roster.objects.get(pk=int(roster_id))
    if request.method == 'GET':
        form = CreateRosterForm(instance=roster)
        return render(request, "rosters/edit_roster.html", {"form": form})
    else:
        form = CreateRosterForm(request.POST, instance=roster)
        form.save()
        return render(request, "groups/groupRosters.html",
                      {"Rosters": list(Roster.objects.filter(Group_id=roster.Group_id))})