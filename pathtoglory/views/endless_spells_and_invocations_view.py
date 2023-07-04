from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect

from ..helpers import user_by_roster_id
from ..models import EndlessSpellsAndInvocations, TheVault
from ..forms import EndlessSpellsAndInvocationsForm
from ..helpers.paths import Paths


@csrf_protect
def endless_spells_and_invocations(request, vault_id):
    form = EndlessSpellsAndInvocationsForm()

    if request.method == 'POST':
        vault = get_object_or_404(TheVault, id=vault_id)
        user_id = user_by_roster_id.get_user_id_by_roster_id(vault.Roster_Id)
        if user_id == request.user.id:
            update_request = request.POST.copy()
            update_request.update({'Vault_Id': vault_id, 'Roster_Id': vault.Roster_Id})
            form = EndlessSpellsAndInvocationsForm(update_request)
            if form.is_valid():
                form.save()
                form = EndlessSpellsAndInvocationsForm()

    spells = list(EndlessSpellsAndInvocations.objects.filter(Vault_Id=vault_id))

    return render(request, Paths.endless_spells_and_invocations, {"form": form, "Vault_Id": vault_id,
                                                                  "vault_item": spells})


@login_required
@csrf_protect
def edit_endless_spells_and_invocations(request, endless_id):
    end = get_object_or_404(EndlessSpellsAndInvocations,  id=endless_id)
    form = EndlessSpellsAndInvocationsForm(instance=end)
    user_id = user_by_roster_id.get_user_id_by_roster_id(end.Roster_Id)
    if request.method == 'POST' and user_id == request.user.id:
        instance = get_object_or_404(EndlessSpellsAndInvocations, id=endless_id)
        form = EndlessSpellsAndInvocationsForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('endless_spells_and_invocations', vault_id=end.Vault_Id.id)

    return render(request, Paths.edit_endless_spells_and_invocations, {"form": form})


@login_required
@csrf_protect
def delete_endless_spells_and_invocations(request, endless_id):
    spell = get_object_or_404(EndlessSpellsAndInvocations, id=endless_id)
    user_id = user_by_roster_id.get_user_id_by_roster_id(spell.Roster_Id)
    if request.method == 'GET' and user_id == request.user.id:
        spell.delete()

    return redirect('endless_spells_and_invocations', vault_id=spell.Vault_Id.id)
