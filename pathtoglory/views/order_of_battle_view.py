from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from ..forms import OrderOfBattleForm
from ..helpers import user_by_roster_id
from ..helpers.paths import Paths
from ..helpers.views_names import Views
from ..models import OrderOfBattle, Warlord, Hero, Unit, EndlessSpellsAndInvocations


@csrf_protect
def order_of_battle(request, roster_id):
    user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)
    try:
        oob = OrderOfBattle.objects.get(Roster_id=roster_id)
    except OrderOfBattle.DoesNotExist:
        oob = None

    form = None

    if oob:
        form = OrderOfBattleForm(instance=oob)

    return render(request, Paths.order_of_battle, {"form": form, "user_id": user_id, "roster_id": roster_id})

@csrf_protect
def order_of_battle_summary(request, roster_id):
    if request.method == 'GET':
        try:
            oob = OrderOfBattle.objects.get(Roster_id=roster_id)
            war_lord = Warlord.objects.get(OrderOfBattle=oob)
            heros = Hero.objects.filter(OrderOfBattle=oob)
            units = Unit.objects.filter(OrderOfBattle=oob)
            endless_spells_and_invocations = EndlessSpellsAndInvocations.objects.filter(Roster_Id=roster_id)

        except OrderOfBattle.DoesNotExist:
            war_lord = None
            heros = None
            units = None
            endless_spells_and_invocations = None

    return render(request, Paths.order_of_battle_summary, {"war_lord": war_lord, "heros": heros, "units": units,\
                                                           "endless_spells_and_invocations": endless_spells_and_invocations})


@login_required
@csrf_protect
def edit_order_of_battle(request, order_of_battle_id):
    oob = get_object_or_404(OrderOfBattle, id=order_of_battle_id)
    user_id = user_by_roster_id.get_user_id_by_roster_id(oob.Roster_id)

    if user_id != request.user.id:
        redirect(Views.home, request)

    form = OrderOfBattleForm(instance=oob)

    if request.method == 'POST':
        form = OrderOfBattleForm(request.POST or None, instance=oob)
        if form.is_valid():
            form.save()
            return redirect('order_of_battle', roster_id=oob.Roster_id)
    else:
        return render(request, Paths.edit_order_of_battle, {"form": form})


@login_required
@csrf_protect
def create_order_of_battle(request, roster_id):
    if request.method == 'POST':
        update_request = request.POST.copy()
        update_request.update({'Roster_id': roster_id})
        form = OrderOfBattleForm(update_request)

        if form.is_valid():
            form.save()
            return redirect('order_of_battle', roster_id=roster_id)

    user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)

    if {request.user.id == user_id}:
        form = OrderOfBattleForm()
        return render(request, Paths.create_order_of_battle, {"form": form})
    else:
        return redirect(Views.home, request)


@login_required
@csrf_protect
def delete_order_of_battle(request, order_of_battle_id):
    return redirect
