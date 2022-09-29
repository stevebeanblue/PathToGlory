from django.shortcuts import render, get_object_or_404, redirect
from ..models import BonusArtifactsOfPower, TheVault
from ..forms import BonusArtifactsOfPowerForm
from ..helpers.paths import Paths


def bonus_artifacts_of_power(request, vault_id):
    form = BonusArtifactsOfPowerForm()

    if request.method == 'POST':
        update_request = request.POST.copy()
        update_request.update({'Vault_Id': vault_id})
        form = BonusArtifactsOfPowerForm(update_request)
        if form.is_valid():
            form.save()
            form = BonusArtifactsOfPowerForm()

    powers = list(BonusArtifactsOfPower.objects.filter(Vault_Id=vault_id))

    return render(request, Paths.bonus_artifacts_of_power, {"form": form, "Vault_Id": vault_id, "vault_item": powers})


def edit_bonus_artifacts_of_power(request, power_id):
    power = BonusArtifactsOfPower.objects.get(id=power_id)
    form = BonusArtifactsOfPowerForm(instance=power)

    if request.method == 'POST':
        instance = get_object_or_404(BonusArtifactsOfPower, id=power_id)
        form = BonusArtifactsOfPowerForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('bonusartifactsofpower', vault_id=power.Vault_Id.id)

    return render(request, Paths.edit_bonus_artifacts_of_power, {"form": form})


def delete_bonus_artifacts_of_power(request, power_id):
    power = get_object_or_404(BonusArtifactsOfPower, id=power_id)
    vault_id = power.Vault_Id.id

    if request.method == 'GET':
        power.delete()

    return redirect('bonusartifactsofpower', vault_id=vault_id)
