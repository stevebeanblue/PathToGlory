from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from ..forms import WarlordForm
from ..helpers import user_by_roster_id
from ..helpers.paths import Paths
from ..models import Warlord, OrderOfBattle


@csrf_protect
def warlord(request, roster_id):
    user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)
    if request.method == 'GET':
        try:
            oob = OrderOfBattle.objects.get(Roster_id=roster_id)
            war_lord = Warlord.objects.get(OrderOfBattle=oob)
            form = WarlordForm(instance=war_lord)
        except Warlord.DoesNotExist:
            form = None

    return render(request, Paths.warlord, {"form": form, "user_id": user_id, "roster_id": roster_id})


@login_required
@csrf_protect
def create_warlord(request, roster_id):
    user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)
    if request.method == 'GET':
        if request.user.id == user_id:
            form = WarlordForm()
        else:
            return redirect('warlord', roster_id)
    else:
        if request.user.id == user_id:
            try:
                oob = OrderOfBattle.objects.get(Roster_id=roster_id)
            except OrderOfBattle.DoesNotExist:
                return redirect('warlord', roster_id)
            update_request = request.POST.copy()
            update_request.update({'OrderOfBattle': oob})
            form = WarlordForm(update_request)
            if form.is_valid():
                form.save()
                return redirect('warlord', roster_id)
        else:
            return redirect('warlord', roster_id)

    return render(request, Paths.create_warlord, {'form': form})


@login_required
@csrf_protect
def edit_warlord(request, roster_id):
    user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)
    if request.user.id == user_id:
        try:
            oob = OrderOfBattle.objects.get(Roster_id=roster_id)
            war_lord = Warlord.objects.get(OrderOfBattle=oob)
        except OrderOfBattle.DoesNotExist or war_lord.DoesNotExist:
            return redirect('warlord', roster_id)

        if request.method == 'GET':
            form = WarlordForm(instance=war_lord)
        else:
            form = WarlordForm(request.POST or None, instance=war_lord)
            if form.is_valid():
                form.save()
                return redirect('warlord', roster_id)

        return render(request, Paths.edit_warlord, {'form': form})
    else:
        return redirect('warlord', roster_id)


@login_required
@csrf_protect
def delete_warlord(request, roster_id):
    if request.method == 'GET':
        user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)
        try:
            oob = OrderOfBattle.objects.get(Roster_id=roster_id)
            war_lord = Warlord.objects.get(OrderOfBattle=oob)
        except OrderOfBattle.DoesNotExist or war_lord.DoesNotExist:
            return redirect('warlord', roster_id)

        if user_id == request.user.id:
            war_lord.delete()

    return redirect('warlord', roster_id)
