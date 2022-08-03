from django.shortcuts import render, get_object_or_404, redirect
from ..models import BonusArtifactsOfPower
from ..forms import BonusArtifactsOfPowerForm
from ..helpers.paths import Paths


def bonus_artifacts_of_power(request, roster_id):
    form = BonusArtifactsOfPowerForm()

    if request.method == 'POST':
        update_request = request.POST.copy()
        update_request.update({'RosterId': roster_id})
        form = BonusArtifactsOfPowerForm(update_request)
        if form.is_valid():
            form.save()
            form = BonusArtifactsOfPowerForm()

    powers = list(BonusArtifactsOfPower.objects.filter(RosterId=roster_id))

    return render(request, Paths.bonusartifactsofpower, {"form": form, "RosterId": roster_id, "powers": powers})


def edit_bonus_artifacts_of_power(request, power_id):
    power = BonusArtifactsOfPower.objects.get_object_or_404(pk=power_id)
    form = BonusArtifactsOfPowerForm(instance=power)

    if request.method == 'POST':
        instance = get_object_or_404(BonusArtifactsOfPower, id=power_id)
        form = BonusArtifactsOfPowerForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('bonus_artifacts_of_power', roster_id=power.RosterId)

    return render(request, Paths.edit_stronghold,
                  {"form": form, "RosterId": power.RosterId})


def delete_bonus_artifacts_of_power(request, power_id):
    power = BonusArtifactsOfPower.objects.get_object_or_404(pk=power_id)
    roster_id = power.RosterId

    if request.method == 'GET':
        power.delete()

    return redirect('bonus_artifacts_of_power', roster_id)