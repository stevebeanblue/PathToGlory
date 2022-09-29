from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from ..models import BonusPrayers
from ..forms import BonusPrayersForm
from ..helpers.paths import Paths


@csrf_protect
def bonus_prayers(request, vault_id):
    form = BonusPrayersForm()

    if request.method == 'POST':
        update_request = request.POST.copy()
        update_request.update({'Vault_Id': vault_id})
        form = BonusPrayersForm(update_request)
        if form.is_valid():
            form.save()
            form = BonusPrayersForm()

    spells = list(BonusPrayers.objects.filter(Vault_Id=vault_id))

    return render(request, Paths.bonus_prayers, {"form": form, "Vault_Id": vault_id,
                                                 "vault_item": spells})


@csrf_protect
def edit_bonus_prayers(request, prayer_id):
    prayer = BonusPrayers.objects.get(id=prayer_id)
    form = BonusPrayersForm(instance=prayer)

    if request.method == 'POST':
        instance = get_object_or_404(BonusPrayers, id=prayer_id)
        form = BonusPrayersForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('bonus_prayers', vault_id=prayer.Vault_Id.id)

    return render(request, Paths.edit_bonus_prayers, {"form": form})


@csrf_protect
def delete_bonus_prayers(request, prayer_id):
    prayer = get_object_or_404(BonusPrayers, id=prayer_id)
    vault_id = prayer.Vault_Id.id

    if request.method == 'GET':
        prayer.delete()

    return redirect('bonus_prayers', vault_id=vault_id)
