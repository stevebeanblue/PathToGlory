from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from ..forms import UnitForm
from ..helpers import user_by_roster_id
from ..helpers.views_names import Views
from ..helpers.paths import Paths
from ..models import Unit, OrderOfBattle


@csrf_protect
def unit(request, roster_id):
    user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)
    if request.method == 'GET':
        try:
            oob = OrderOfBattle.objects.get(Roster_id=roster_id)
            units = list(Unit.objects.filter(OrderOfBattle=oob))
            form = UnitForm()
        except Unit.DoesNotExist or OrderOfBattle.DoesNotExist:
            form = None
    else:
        if request.user.id == user_id:
            try:
                oob = OrderOfBattle.objects.get(Roster_id=roster_id)
                units = list(Unit.objects.filter(OrderOfBattle=oob))
            except OrderOfBattle.DoesNotExist:
                return redirect('order_of_battle', roster_id)
            update_request = request.POST.copy()
            update_request.update({'OrderOfBattle': oob})
            form = UnitForm(update_request)
            if form.is_valid():
                form.save()
                return redirect('unit', roster_id)
        else:
            return redirect('OrderOfBattle', roster_id)

    return render(request, Paths.unit, {"form": form, "user_id": user_id, "roster_id": roster_id, "units": units})


@csrf_protect
def edit_unit(request, unit_id):
    try:
        unit = Unit.objects.get(id=unit_id)
        oob = OrderOfBattle.objects.get(Roster_id=unit.OrderOfBattle.Roster_id)
    except OrderOfBattle.DoesNotExist or unit.DoesNotExist:
        return redirect(Views.home)

    user_id = user_by_roster_id.get_user_id_by_roster_id(oob.Roster_id)

    if request.user.id == user_id:
        if request.method == 'GET':
            form = UnitForm(instance=unit)
        else:
            form = UnitForm(request.POST or None, instance=unit)
            if form.is_valid():
                form.save()
                return redirect('unit', oob.Roster_id)

        return render(request, Paths.edit_unit, {'form': form})
    else:
        return redirect('unit', oob.Roster_id)


@csrf_protect
def delete_unit(request, unit_id):
    if request.method == 'GET':
        try:
            unit = Unit.objects.get(id=unit_id)
            oob = OrderOfBattle.objects.get(Roster_id=unit.OrderOfBattle.Roster_id)
        except OrderOfBattle.DoesNotExist or Unit.DoesNotExist:
            return redirect('unit', oob.Roster_id)
        user_id = user_by_roster_id.get_user_id_by_roster_id(oob.Roster_id)
        if user_id == request.user.id:
            unit.delete()

        return redirect('unit', oob.Roster_id)

    return redirect(Views.home)

