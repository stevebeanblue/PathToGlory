from django.shortcuts import render, get_object_or_404, redirect
from ..models import BonusArtifactsOfPower, TheVault, BonusUniqueEnhancements
from ..forms import BonusUniqueEnhancementsForm
from ..helpers.paths import Paths


def bonus_unique_enhancement(request, vault_id):
    form = BonusUniqueEnhancementsForm()

    if request.method == 'POST':
        update_request = request.POST.copy()
        update_request.update({'Vault_Id': vault_id})
        form = BonusUniqueEnhancementsForm(update_request)
        if form.is_valid():
            form.save()
            form = BonusUniqueEnhancementsForm()

    enhancements = list(BonusUniqueEnhancements.objects.filter(Vault_Id=vault_id))

    return render(request, Paths.bonus_unique_enhancement, {"form": form, "Vault_Id": vault_id,
                                                            "vault_item": enhancements})


def edit_bonus_unique_enhancement(request, unique_id):
    power = BonusUniqueEnhancements.objects.get(id=unique_id)
    form = BonusUniqueEnhancementsForm(instance=power)

    if request.method == 'POST':
        instance = get_object_or_404(BonusUniqueEnhancements, id=unique_id)
        form = BonusUniqueEnhancementsForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('bonus_unique_enhancement', vault_id=power.Vault_Id.id)

    return render(request, Paths.edit_bonus_unique_enhancement, {"form": form})


def delete_bonus_unique_enhancement(request, unique_id):
    power = get_object_or_404(BonusUniqueEnhancements, id=unique_id)
    vault_id = power.Vault_Id.id

    if request.method == 'GET':
        power.delete()

    return redirect('bonus_unique_enhancement', vault_id=vault_id)
