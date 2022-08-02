from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from ..models import Achievements, Roster
from ..forms import AchievementsForm
from ..helpers.paths import Paths

def create_achievements(request, roster_id):
    form = AchievementsForm()

    instance = Achievements.objects.filter(RosterId=roster_id)

    if instance:
        return redirect('viewachievement', roster_id)

    if request.method == 'POST':
        update_request = request.POST.copy()
        update_request.update({'RosterId': roster_id})
        form = AchievementsForm(update_request)
        if form.is_valid():
            form.save()
            roster = Roster.objects.get(pk=roster_id)
            return redirect('grouprosters', group_id=roster.Group_id_as_int)

    return render(request, Paths.create_achievement,
                  {"form": form, "RosterId": roster_id})


def view_achievement(request, roster_id):
    instance = Achievements.objects.get(RosterId=roster_id)

    if instance:
        form = AchievementsForm(instance=instance)

    return render(request, Paths.view_achievement, {"form": form, "RosterId": roster_id})


def edit_achievements(request, roster_id):
    achievement = Achievements.objects.get(RosterId=roster_id)
    form = AchievementsForm(instance=achievement)

    if request.method == 'POST':
        instance = get_object_or_404(Achievements, RosterId=roster_id)
        form = AchievementsForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            roster = Roster.objects.get(pk=roster_id)
            return redirect('grouprosters', group_id=roster.Group_id_as_int)

    return render(request, Paths.edit_achievement,
                  {"form": form, "RosterId": roster_id})