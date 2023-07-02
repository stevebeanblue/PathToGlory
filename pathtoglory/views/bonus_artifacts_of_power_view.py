from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect

from ..helpers import user_by_roster_id
from ..models import BonusArtifactsOfPower, TheVault
from ..forms import BonusArtifactsOfPowerForm
from ..helpers.paths import Paths


def bonus_artifacts_of_power(request, vault_id):
    form = BonusArtifactsOfPowerForm()

    if request.method == 'POST':
        vault = get_object_or_404(TheVault, id=vault_id)
        user_id = user_by_roster_id.get_user_id_by_roster_id(vault.Roster_Id)
        if user_id == request.user.id:
            update_request = request.POST.copy()
            update_request.update({'Vault_Id': vault_id, 'Roster_Id': vault.Roster_Id})
            form = BonusArtifactsOfPowerForm(update_request)
            if form.is_valid():
                form.save()
                form = BonusArtifactsOfPowerForm()

    powers = list(BonusArtifactsOfPower.objects.filter(Vault_Id=vault_id))

    return render(request, Paths.bonus_artifacts_of_power, {"form": form, "Vault_Id": vault_id, "vault_item": powers})


@login_required
@csrf_protect
def edit_bonus_artifacts_of_power(request, power_id):
    power = get_object_or_404(BonusArtifactsOfPower, id=power_id)
    form = BonusArtifactsOfPowerForm(instance=power)
    user_id = user_by_roster_id.get_user_id_by_roster_id(power.Roster_Id)

    if request.method == 'POST' and user_id == request.user.id:
        instance = get_object_or_404(BonusArtifactsOfPower, id=power_id)
        form = BonusArtifactsOfPowerForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('bonusartifactsofpower', vault_id=power.Vault_Id.id)

    return render(request, Paths.edit_bonus_artifacts_of_power, {"form": form})


@login_required
@csrf_protect
def delete_bonus_artifacts_of_power(request, power_id):
    power = get_object_or_404(BonusArtifactsOfPower, id=power_id)
    vault_id = power.Vault_Id.id
    user_id = user_by_roster_id.get_user_id_by_roster_id(power.Roster_Id)

    if request.method == 'GET' and user_id == request.user.id:
        power.delete()

    return redirect('bonusartifactsofpower', vault_id=vault_id)
