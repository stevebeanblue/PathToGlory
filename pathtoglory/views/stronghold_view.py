from django.shortcuts import render, get_object_or_404, redirect
from ..models import Stronghold
from ..forms import StrongholdForm
from ..helpers.paths import Paths


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