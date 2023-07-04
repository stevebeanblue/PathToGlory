from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from ..forms import HeroForm
from ..helpers import user_by_roster_id
from ..helpers.views_names import Views
from ..helpers.paths import Paths
from ..models import Hero, OrderOfBattle


@csrf_protect
def hero(request, roster_id):
    user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)
    heros = None
    if request.method == 'GET':
        try:
            oob = OrderOfBattle.objects.get(Roster_id=roster_id)
            heros = list(Hero.objects.filter(OrderOfBattle=oob))
            form = HeroForm()
        except Hero.DoesNotExist or OrderOfBattle.DoesNotExist:
            form = None
    else:
        if request.user.id == user_id:
            try:
                oob = OrderOfBattle.objects.get(Roster_id=roster_id)
            except OrderOfBattle.DoesNotExist:
                return redirect('hero', roster_id)
            update_request = request.POST.copy()
            update_request.update({'OrderOfBattle': oob})
            form = HeroForm(update_request)
            if form.is_valid():
                form.save()
                return redirect('hero', roster_id)
        else:
            return redirect('hero', roster_id)

    return render(request, Paths.hero, {"form": form, "user_id": user_id, "roster_id": roster_id, "heros": heros})


@login_required
@csrf_protect
def edit_hero(request, hero_id):
    try:
        hero = Hero.objects.get(id=hero_id)
        oob = OrderOfBattle.objects.get(Roster_id=hero.OrderOfBattle.Roster_id)
    except OrderOfBattle.DoesNotExist or Hero.DoesNotExist:
        return redirect(Views.home)

    user_id = user_by_roster_id.get_user_id_by_roster_id(oob.Roster_id)

    if request.user.id == user_id:
        if request.method == 'GET':
            form = HeroForm(instance=hero)
        else:
            form = HeroForm(request.POST or None, instance=hero)
            if form.is_valid():
                form.save()
                return redirect('hero', oob.Roster_id)

        return render(request, Paths.edit_hero, {'form': form})
    else:
        return redirect('hero', oob.Roster_id)


@login_required
@csrf_protect
def delete_hero(request, hero_id):
    if request.method == 'GET':
        try:
            hero = Hero.objects.get(id=hero_id)
            oob = OrderOfBattle.objects.get(Roster_id=hero.OrderOfBattle.Roster_id)
        except OrderOfBattle.DoesNotExist or Hero.DoesNotExist:
            return redirect('hero', oob.Roster_id)
        user_id = user_by_roster_id.get_user_id_by_roster_id(oob.Roster_id)
        if user_id == request.user.id:
            hero.delete()

        return redirect('hero', oob.Roster_id)

    return redirect(Views.home)

