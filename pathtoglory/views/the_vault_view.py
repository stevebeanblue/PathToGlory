from django.shortcuts import render, get_object_or_404, redirect
from ..models import TheVault, Roster, BonusArtifactsOfPower, BonusUniqueEnhancements, \
    BonusSpells, BonusPrayers, EndlessSpellsAndInvocations, Battalions
from ..forms import BonusArtifactsOfPowerForm, BonusUniqueEnhancementsForm, BonusSpellsForm, \
    BonusPrayersForm, EndlessSpellsAndInvocationsForm, BattalionsForm
from ..helpers.paths import Paths

def the_vault(request, roster_id):

    if request.POST:
        roster = Roster.objects.get(pk=roster_id)
        if roster.User_id == request.user.id:
            data = {
                'Roster_Id':roster_id,
                'Name':"Add name"
            }
            art_of_power = BonusArtifactsOfPowerForm(data)
            unique_enhance = BonusUniqueEnhancementsForm(data)
            bonus_spell = BonusSpellsForm(data)
            prayer = BonusPrayersForm(data)
            invo = EndlessSpellsAndInvocationsForm(data)
            bat = BattalionsForm(data)
            TheVault.objects.get_or_create(Roster_Id=roster_id,
                                           Triumph="Add triumph",
                                           BonusArtifactsOfPower=art_of_power.save(),
                                           BonusUniqueEnhancements=unique_enhance.save(),
                                           BonusSpells=bonus_spell.save(),
                                           BonusPrayers=prayer.save(),
                                           EndlessSpellsAndInvocations=invo.save(),
                                           Battalions=bat.save())

    try:
        vault = TheVault.objects.get(RosterId=roster_id)
    except:
        vault = None
        roster = Roster.objects.get(pk=roster_id)

    return render(request, Paths.the_vault, {"vault": vault, "user_id": roster.User_id})


def create_vault_objects(obj, roster_id):
    form = obj
    form.Roster_Id = roster_id
    form.save()