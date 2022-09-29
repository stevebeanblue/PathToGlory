from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from ..models import EndlessSpellsAndInvocations
from ..forms import EndlessSpellsAndInvocationsForm
from ..helpers.paths import Paths


@csrf_protect
def endless_spells_and_invocations(request, vault_id):
    form = EndlessSpellsAndInvocationsForm()

    if request.method == 'POST':
        update_request = request.POST.copy()
        update_request.update({'Vault_Id': vault_id})
        form = EndlessSpellsAndInvocationsForm(update_request)
        if form.is_valid():
            form.save()
            form = EndlessSpellsAndInvocationsForm()

    spells = list(EndlessSpellsAndInvocations.objects.filter(Vault_Id=vault_id))

    return render(request, Paths.endless_spells_and_invocations, {"form": form, "Vault_Id": vault_id,
                                                                  "vault_item": spells})


@csrf_protect
def edit_endless_spells_and_invocations(request, endless_id):
    end = EndlessSpellsAndInvocations.objects.get(id=endless_id)
    form = EndlessSpellsAndInvocationsForm(instance=end)

    if request.method == 'POST':
        instance = get_object_or_404(EndlessSpellsAndInvocations, id=endless_id)
        form = EndlessSpellsAndInvocationsForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('endless_spells_and_invocations', vault_id=end.Vault_Id.id)

    return render(request, Paths.edit_endless_spells_and_invocations, {"form": form})


@csrf_protect
def delete_endless_spells_and_invocations(request, endless_id):
    spell = get_object_or_404(EndlessSpellsAndInvocations, id=endless_id)
    vault_id = spell.Vault_Id.id

    if request.method == 'GET':
        spell.delete()

    return redirect('endless_spells_and_invocations', vault_id=vault_id)
