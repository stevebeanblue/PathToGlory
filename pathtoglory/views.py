from django.shortcuts import render
from .models import PathToGloryGroup, Roster, QuestLog
from .forms import CreateRosterForm, QuestLogForm


def home(request):
    if request.method == 'GET':
        return render(request, "home.html", {"PathToGloryGroup": list(PathToGloryGroup.objects.all())})


def grouprosters(request, group_id):
    if request.method == 'GET':
        return render(request, "groups/groupRosters.html",
                      {"Rosters": list(Roster.objects.filter(Group_id=group_id))})


def createroster(request):
    if request.method == 'GET':
        return render(request, "rosters/create_roster.html", {"form": CreateRosterForm()})
    else:
        form = CreateRosterForm(request.POST)
        form.save()
        return home(request)


def editroster(request, roster_id):
    try:
        roster = Roster.objects.get(pk=int(roster_id))
    except Roster.DoesNotExist:
        return home(request)

    if not roster or request.user.id != roster.User.id:
        return home(request)

    if request.method == 'GET':
        form = CreateRosterForm(instance=roster)
        return render(request, "rosters/edit_roster.html", {"form": form, "RosterId": roster_id})
    else:
        form = CreateRosterForm(request.POST, instance=roster)
        form.save()
        return render(request, "groups/groupRosters.html",
                      {"Rosters": list(Roster.objects.filter(Group_id=roster.Group_id))})


def createquestlog(request, roster_id):
    if request.method == 'GET':
        form = QuestLogForm()
        form.RosterId = roster_id
        return render(request, "rosters/questlog/create_questlog.html", {"form": form, "RosterId": roster_id})
    else:
        #add validation to only be able to have one quest per roster
        form = QuestLogForm(request.POST)
        form.RosterId = roster_id
        form.save()
        return home(request)
