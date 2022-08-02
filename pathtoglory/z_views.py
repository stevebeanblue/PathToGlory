from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import PathToGloryGroup, Roster, QuestLog, Stronghold, Achievements, BonusArtifactsOfPower, TheVault
from .forms import CreateRosterForm, QuestLogForm, StrongholdForm, AchievementsForm, BonusArtifactsOfPowerForm
from .helpers.paths import Paths




def createstronghold(request, roster_id):
    form = StrongholdForm()

    if request.method == 'POST':
        update_request = request.POST.copy()
        update_request.update({'RosterId': roster_id})
        form = StrongholdForm(update_request)
        if form.is_valid():
            form.save()
            form = StrongholdForm()

    strongholds = list(Stronghold.objects.filter(RosterId=roster_id))

    return render(request, Paths.create_stronghold, {"form": form, "RosterId": roster_id, "strongholds": strongholds})


def edit_stronghold(request, stronghold_id):
    stronghold = Stronghold.objects.get(pk=stronghold_id)
    form = StrongholdForm(instance=stronghold)

    if request.method == 'POST':
        instance = get_object_or_404(Stronghold, id=stronghold_id)
        form = StrongholdForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('createstronghold', roster_id=stronghold.RosterId)

    return render(request, Paths.edit_stronghold,
                  {"form": form, "RosterId": stronghold.RosterId})


def delete_stronghold(request, stronghold_id):
    stronghold = Stronghold.objects.get(pk=stronghold_id)
    roster_id = stronghold.RosterId

    if request.method == 'GET':
        stronghold.delete()

    return redirect('createstronghold', roster_id)





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
    power = BonusArtifactsOfPower.objects.get(pk=power_id)
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
    power = BonusArtifactsOfPower.objects.get(pk=power_id)
    roster_id = power.RosterId

    if request.method == 'GET':
        power.delete()

    return redirect('bonus_artifacts_of_power', roster_id)


def the_vault(request, roster_id):
    #vault = TheVault.objects.get_or_create(RosterId=roster_id)
    return render(request, Paths.the_vault, {"vault": ""})
