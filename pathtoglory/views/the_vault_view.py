from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404

from ..forms import TheVaultForm
from ..helpers import user_by_roster_id
from ..helpers.paths import Paths
from ..helpers.views_names import Views
from ..models import TheVault


def the_vault(request, roster_id):

    user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)

    if request.method == 'GET':
        try:
            vault = TheVault.objects.get(Roster_Id=roster_id)
            form = TheVaultForm(instance=vault)
            vault_id = vault.id
        except ObjectDoesNotExist:
            form = None
            vault_id = 0

        return render(request, Paths.the_vault, {"form": form, "user_id": user_id, "roster_id": roster_id,
                                                 "vault_id": vault_id})
    else:
        return redirect(Views.home)


def create_vault(request, roster_id):

    user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)

    if request.user.id == user_id:
        if request.method == 'POST':
            update_request = request.POST.copy()
            update_request.update({'Roster_Id': roster_id})
            form = TheVaultForm(update_request)
            if form.is_valid():
                form.save()
                vault_id = TheVault.objects.get(Roster_Id=roster_id).id
                return render(request, Paths.the_vault,
                              {"form": form, "user_id": user_id, "vault_id": vault_id, "roster_id": roster_id})
        else:
            form = TheVaultForm()

        return render(request, Paths.create_vault, {"form": form, "user_id": user_id, "vault_id": 0,
                                                    "roster_id": roster_id})
    else:
        return redirect(Views.home)


def edit_vault(request, vault_id):

    vault = get_object_or_404(TheVault, pk=vault_id)
    user_id = user_by_roster_id.get_user_id_by_roster_id(vault.Roster_Id)

    if request.user.id == user_id:
        form = TheVaultForm(instance=vault)
        if request.method == 'POST':
            form = TheVaultForm(request.POST or None, instance=vault)
            if form.is_valid():
                form.save()
                return redirect(Views.the_vault, roster_id=vault.Roster_Id)

        return render(request, Paths.edit_vault, {"form": form, "user_id": user_id, "vault_id": vault_id})
    else:
        return redirect(Views.home)


def delete_vault(request, roster_id):

    user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)

    if request.method == 'GET':
        if user_id == request.user.id:
            vault = get_object_or_404(TheVault, Roster_Id=roster_id)
            vault.delete()

    return redirect('thevault', roster_id)
