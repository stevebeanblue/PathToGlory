from django.shortcuts import render
from ..models import Roster, PathToGloryGroup
from ..helpers.paths import Paths
from ..forms import CreateRosterForm


def grouprosters(request, group_id):
    if request.method == 'GET':
        return render(request, Paths.group_rosters,
                      {"Rosters": list(Roster.objects.filter(Group_id=group_id))})


def createroster(request):
    if request.method == 'GET':
        form = CreateRosterForm()
        return render(request, Paths.create_roster, {"form": form})
    else:
        update_request = request.POST.copy()
        update_request.update({'User_id': request.user.id, 'DateCreated': datetime.now(), 'PlayerName': request.user,
                               'Group_id_as_int': request.POST.get("Group_id")})
        form = CreateRosterForm(update_request)
        if form.is_valid():
            form.save()
        else:
            return render(request, Paths.create_roster, {"form": form})
        return render(request, Paths.home, {"PathToGloryGroup": list(PathToGloryGroup.objects.all())})


def editroster(request, roster_id):
    try:
        roster = Roster.objects.get(pk=int(roster_id))
    except Roster.DoesNotExist:
        return home(request)

    if not roster or request.user.id != roster.User_id:
        return home(request)

    if request.method == 'GET':
        form = CreateRosterForm(instance=roster)
        return render(request, Paths.edit_roster, {"form": form, "RosterId": roster_id})
    else:
        form = CreateRosterForm(request.POST, instance=roster)
        form.save()
        return render(request, Paths.group_rosters,
                      {"Rosters": list(Roster.objects.filter(Group_id=roster.Group_id))})