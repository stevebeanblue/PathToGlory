from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect

from ..helpers import user_by_roster_id
from ..models import Battalions, TheVault
from ..forms import BattalionsForm
from ..helpers.paths import Paths


@csrf_protect
def battalions(request, vault_id):
    form = BattalionsForm()
    vault = get_object_or_404(TheVault, id=vault_id)
    user_id = user_by_roster_id.get_user_id_by_roster_id(vault.Roster_Id)

    if user_id == request.user.id and request.method == 'POST':
        update_request = request.POST.copy()
        update_request.update({'Vault_Id': vault_id, 'Roster_Id': vault.Roster_Id})
        form = BattalionsForm(update_request)
        if form.is_valid():
            form.save()
            form = BattalionsForm()

    battalion = list(Battalions.objects.filter(Vault_Id=vault_id))

    return render(request, Paths.battalions, {"form": form, "Vault_Id": vault_id,
                                              "vault_item": battalion})


@login_required
@csrf_protect
def edit_battalion(request, battalion_id):
    battalion = get_object_or_404(Battalions, id=battalion_id)
    user_id = user_by_roster_id.get_user_id_by_roster_id(battalion.Roster_Id)
    form = BattalionsForm(instance=battalion)

    if user_id == request.user.id:
        if request.method == 'POST':
            instance = get_object_or_404(Battalions, id=battalion_id)
            form = BattalionsForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('battalions', vault_id=battalion.Vault_Id.id)

        return render(request, Paths.edit_battalions, {"form": form})
    else:
        return render(request, Paths.battalions, {"form": form, "Vault_Id": battalion.Vault_Id,
                                                  "vault_item": battalion})


@login_required
@csrf_protect
def delete_battalion(request, battalion_id):

    battalion = get_object_or_404(Battalions, id=battalion_id)
    vault_id = battalion.Vault_Id.id
    user_id = user_by_roster_id.get_user_id_by_roster_id(battalion.Roster_Id)

    if user_id == request.user.id:
        if request.method == 'GET':
            battalion.delete()

    return redirect('battalions', vault_id=vault_id)
