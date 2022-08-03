from django.shortcuts import render, get_object_or_404, redirect
from ..models import TheVault, Roster
#from ..forms import StrongholdForm
from ..helpers.paths import Paths

def the_vault(request, roster_id):

    if request.POST:
        this = 1

    try:
        vault = TheVault.objects.get_or_create(RosterId=roster_id)
    except:
        vault = None
        roster = Roster.objects.get(pk=roster_id)

    return render(request, Paths.the_vault, {"vault": vault, "user_id": roster.User_id})