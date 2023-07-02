from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect

from ..helpers import user_by_roster_id
from ..models import BonusPrayers, TheVault
from ..forms import BonusPrayersForm
from ..helpers.paths import Paths


@csrf_protect
def bonus_prayers(request, vault_id):
    form = BonusPrayersForm()

    if request.method == 'POST':
        vault = get_object_or_404(TheVault, id=vault_id)
        user_id = user_by_roster_id.get_user_id_by_roster_id(vault.Roster_Id)
        if user_id == request.user.id:
            update_request = request.POST.copy()
            update_request.update({'Vault_Id': vault_id, 'Roster_Id': vault.Roster_Id})
            form = BonusPrayersForm(update_request)
            if form.is_valid():
                form.save()
                form = BonusPrayersForm()

    spells = list(BonusPrayers.objects.filter(Vault_Id=vault_id))

    return render(request, Paths.bonus_prayers, {"form": form, "Vault_Id": vault_id,
                                                 "vault_item": spells})


@login_required
@csrf_protect
def edit_bonus_prayers(request, prayer_id):
    prayer = get_object_or_404(BonusPrayers, id=prayer_id)
    form = BonusPrayersForm(instance=prayer)
    user_id = user_by_roster_id.get_user_id_by_roster_id(prayer.Roster_Id)
    if request.method == 'POST' and user_id == request.user.id:
        form = BonusPrayersForm(request.POST or None, instance=prayer)
        if form.is_valid():
            form.save()
            return redirect('bonus_prayers', vault_id=prayer.Vault_Id.id)

    return render(request, Paths.edit_bonus_prayers, {"form": form})


@login_required
@csrf_protect
def delete_bonus_prayers(request, prayer_id):
    prayer = get_object_or_404(BonusPrayers, id=prayer_id)
    user_id = user_by_roster_id.get_user_id_by_roster_id(prayer.Roster_Id)
    if request.method == 'GET' and user_id == request.user.id:
        prayer.delete()

    return redirect('bonus_prayers', vault_id=prayer.Vault_Id.id)
