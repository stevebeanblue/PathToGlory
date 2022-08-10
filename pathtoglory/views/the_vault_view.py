from django.shortcuts import render, get_object_or_404, redirect
from ..models import TheVault, Roster
from ..forms import TheVaultForm
from ..helpers.paths import Paths
from ..helpers.user_by_roster_id import get_user_id_by_roster_id

def the_vault(request, roster_id):

    user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)

    if request.method == 'GET':
        try:
            form = TheVaultForm.objects.get(Roster_Id=roster_id)
        except:
            form = None()

    return render(request, Paths.the_vault, {"form": form, "user_id": user_id, "roster_id": roster_id})


def create_vault(request, roster_id):

    user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)

    if request.user.id == user_id:
        if request.method == 'POST':
            update_request = request.POST.copy()
            update_request.update({'Roster_Id': roster_id})
            form = TheVaultForm(update_request)
            if form.is_valid():
                form.save()
                return redirect(request, Paths.the_vault, {"form": form, "user_id": user_id})
    else:
        return redirect(request, Paths.home)


def edit_vault(request, vault_id):
    user_id = user_by_roster_id.get_user_id_by_roster_id(vault.Roster_Id)

    if request.user.id == user_id:
        vault = TheVault.objects.get(pk=vault_id)
        form = TheVaultForm(instane=vault)
        if request.method == 'POST':
            instance = get_object_or_404(TheVault, pk=vault_id)
            form = TheVaultForm(instance=instance)
            if form.is_valid():
                form.save()
                return redirect(request, Paths.the_vault, {"form": form, "user_id": user_id})

        return render(request, Paths.edit_vault, {"form": form, "user_id": user_id})
    else:
        return redirect(request, Paths.home)
