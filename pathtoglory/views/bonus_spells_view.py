from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect

from ..helpers import user_by_roster_id
from ..models import BonusSpells, TheVault
from ..forms import BonusSpellsForm
from ..helpers.paths import Paths


@csrf_protect
def bonus_spell(request, vault_id):
    form = BonusSpellsForm()

    if request.method == 'POST':
        vault = get_object_or_404(TheVault, id=vault_id)
        user_id = user_by_roster_id.get_user_id_by_roster_id(vault.Roster_Id)
        if user_id == request.user.id:
            update_request = request.POST.copy()
            update_request.update({'Vault_Id': vault_id, 'Roster_Id': vault.Roster_Id})
            form = BonusSpellsForm(update_request)
            if form.is_valid():
                form.save()
                form = BonusSpellsForm()

    spells = list(BonusSpells.objects.filter(Vault_Id=vault_id))

    return render(request, Paths.bonus_spells, {"form": form, "Vault_Id": vault_id,
                                                "vault_item": spells})


@login_required
@csrf_protect
def edit_bonus_spell(request, spell_id):
    spell = BonusSpells.objects.get(id=spell_id)
    form = BonusSpellsForm(instance=spell)
    user_id = user_by_roster_id.get_user_id_by_roster_id(spell.Roster_Id)
    if request.method == 'POST' and user_id == request.user.id:
        form = BonusSpellsForm(request.POST or None, instance=spell)
        if form.is_valid():
            form.save()
            return redirect('bonus_spells', vault_id=spell.Vault_Id.id)

    return render(request, Paths.edit_bonus_spell, {"form": form})


@login_required
@csrf_protect
def delete_bonus_spell(request, spell_id):
    spell = get_object_or_404(BonusSpells, id=spell_id)
    user_id = user_by_roster_id.get_user_id_by_roster_id(spell.Roster_Id)
    if request.method == 'GET' and user_id == request.user.id:
        spell.delete()

    return redirect('bonus_spells', vault_id=spell.Vault_Id.id)
