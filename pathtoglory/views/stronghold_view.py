from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect

from ..helpers import user_by_roster_id
from ..models import Stronghold
from ..forms import StrongholdForm
from ..helpers.paths import Paths


@csrf_protect
def createstronghold(request, roster_id):
    form = StrongholdForm()

    if request.method == 'POST':
        user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)
        if user_id == request.user.id:
            update_request = request.POST.copy()
            update_request.update({'RosterId': roster_id})
            form = StrongholdForm(update_request)
            if form.is_valid():
                form.save()
                form = StrongholdForm()

    strongholds = list(Stronghold.objects.filter(RosterId=roster_id))

    return render(request, Paths.create_stronghold, {"form": form, "RosterId": roster_id, "strongholds": strongholds})


@login_required
@csrf_protect
def edit_stronghold(request, stronghold_id):
    stronghold = get_object_or_404(Stronghold, id=stronghold_id)
    form = StrongholdForm(instance=stronghold)
    user_id = user_by_roster_id.get_user_id_by_roster_id(stronghold.RosterId)

    if request.method == 'POST' and user_id == request.user.id:
        form = StrongholdForm(request.POST or None, instance=stronghold)
        if form.is_valid():
            form.save()
            return redirect('createstronghold', roster_id=stronghold.RosterId)

    return render(request, Paths.edit_stronghold,
                  {"form": form, "RosterId": stronghold.RosterId})


@login_required
@csrf_protect
def delete_stronghold(request, stronghold_id):
    stronghold = get_object_or_404(Stronghold, id=stronghold_id)
    user_id = user_by_roster_id.get_user_id_by_roster_id(stronghold.RosterId)

    if request.method == 'GET' and user_id == request.user.id:
        stronghold.delete()

    return redirect('createstronghold', stronghold.RosterId)