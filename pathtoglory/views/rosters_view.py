from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from ..models import Roster, PathToGloryGroup
from ..helpers.paths import Paths
from ..forms import CreateRosterForm


@csrf_protect
def grouprosters(request, group_id):
    if request.method == 'GET':
        return render(request, Paths.group_rosters,
                      {"Rosters": list(Roster.objects.filter(Group_id=group_id))})


@csrf_protect
def my_rosters(request):
    if request.method == 'GET':
        return render(request, Paths.group_rosters, {"Rosters": list(Roster.objects.filter(User_id=request.user.id))})


@csrf_protect
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
            return redirect('my_rosters')
        else:
            return render(request, Paths.create_roster, {"form": form})

        return render(request, Paths.home, {"PathToGloryGroup": list(PathToGloryGroup.objects.all())})


@csrf_protect
def editroster(request, roster_id):
    try:
        roster = Roster.objects.get(pk=int(roster_id))
    except Roster.DoesNotExist:
        return redirect('home', request)

    if not roster or request.user.id != roster.User_id:
        return redirect('home', request)

    if request.method == 'GET':
        form = CreateRosterForm(instance=roster)
        return render(request, Paths.edit_roster, {"form": form, "RosterId": roster_id})
    else:
        form = CreateRosterForm(request.POST, instance=roster)
        form.save()
        return render(request, Paths.group_rosters,
                      {"Rosters": list(Roster.objects.filter(Group_id=roster.Group_id))})


@csrf_protect
def delete_roster(request, roster_id):
    roster = get_object_or_404(Roster, id=roster_id)

    if request.method == 'GET':
        roster.delete()

    return redirect('my_rosters')
