from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from ..models import BonusSpells
from ..forms import BonusSpellsForm
from ..helpers.paths import Paths


@csrf_protect
def bonus_spell(request, vault_id):
    form = BonusSpellsForm()

    if request.method == 'POST':
        update_request = request.POST.copy()
        update_request.update({'Vault_Id': vault_id})
        form = BonusSpellsForm(update_request)
        if form.is_valid():
            form.save()
            form = BonusSpellsForm()

    spells = list(BonusSpells.objects.filter(Vault_Id=vault_id))

    return render(request, Paths.bonus_spells, {"form": form, "Vault_Id": vault_id,
                                                "vault_item": spells})


@csrf_protect
def edit_bonus_spell(request, spell_id):
    spell = BonusSpells.objects.get(id=spell_id)
    form = BonusSpellsForm(instance=spell)

    if request.method == 'POST':
        instance = get_object_or_404(BonusSpells, id=spell_id)
        form = BonusSpellsForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('bonus_spells', vault_id=spell.Vault_Id.id)

    return render(request, Paths.edit_bonus_spell, {"form": form})


@csrf_protect
def delete_bonus_spell(request, spell_id):
    spell = get_object_or_404(BonusSpells, id=spell_id)
    vault_id = spell.Vault_Id.id

    if request.method == 'GET':
        spell.delete()

    return redirect('bonus_spells', vault_id=vault_id)
