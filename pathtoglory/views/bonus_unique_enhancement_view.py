from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect

from ..helpers import user_by_roster_id
from ..models import BonusArtifactsOfPower, TheVault, BonusUniqueEnhancements
from ..forms import BonusUniqueEnhancementsForm
from ..helpers.paths import Paths


@csrf_protect
def bonus_unique_enhancement(request, vault_id):
    form = BonusUniqueEnhancementsForm()

    if request.method == 'POST':
        vault = get_object_or_404(TheVault, id=vault_id)
        user_id = user_by_roster_id.get_user_id_by_roster_id(vault.Roster_Id)
        if user_id == request.user.id:
            update_request = request.POST.copy()
            update_request.update({'Vault_Id': vault_id, 'Roster_Id': vault.Roster_Id})
            form = BonusUniqueEnhancementsForm(update_request)
            if form.is_valid():
                form.save()
                form = BonusUniqueEnhancementsForm()

    enhancements = list(BonusUniqueEnhancements.objects.filter(Vault_Id=vault_id))

    return render(request, Paths.bonus_unique_enhancement, {"form": form, "Vault_Id": vault_id,
                                                            "vault_item": enhancements})


@login_required
@csrf_protect
def edit_bonus_unique_enhancement(request, unique_id):
    power = get_object_or_404(BonusUniqueEnhancements, id=unique_id)
    form = BonusUniqueEnhancementsForm(instance=power)
    user_id = user_by_roster_id.get_user_id_by_roster_id(power.Roster_Id)
    if request.method == 'POST' and user_id == request.user.id:
        form = BonusUniqueEnhancementsForm(request.POST or None, instance=power)
        if form.is_valid():
            form.save()
            return redirect('bonus_unique_enhancement', vault_id=power.Vault_Id.id)

    return render(request, Paths.edit_bonus_unique_enhancement, {"form": form})


@login_required
@csrf_protect
def delete_bonus_unique_enhancement(request, unique_id):
    power = get_object_or_404(BonusUniqueEnhancements, id=unique_id)
    vault_id = power.Vault_Id.id
    user_id = user_by_roster_id.get_user_id_by_roster_id(power.Roster_Id)
    if request.method == 'GET' and user_id == request.user.id:
        power.delete()

    return redirect('bonus_unique_enhancement', vault_id=vault_id)
