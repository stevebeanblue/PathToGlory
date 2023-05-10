from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from django.views.decorators.csrf import csrf_protect

from ..helpers import user_by_roster_id
from ..models import Achievements, Roster
from ..forms import AchievementsForm
from ..helpers.paths import Paths


@csrf_protect
@login_required
def create_achievements(request, roster_id):

    user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)

    if request.user.id == user_id:

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
    else:
        return render(request, Paths.home)


def view_achievement(request, roster_id):

    instance = get_object_or_404(Achievements, RosterId=roster_id)

    form = AchievementsForm(instance=instance)

    return render(request, Paths.view_achievement, {"form": form, "RosterId": roster_id})


@csrf_protect
@login_required
def edit_achievements(request, roster_id):

    user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)

    if request.user.id == user_id:

        if request.method == 'POST':
            instance = get_object_or_404(Achievements, RosterId=roster_id)
            form = AchievementsForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('viewachievement', roster_id=roster_id)

        achievement = get_object_or_404(Achievements, RosterId=roster_id)
        form = AchievementsForm(instance=achievement)

        return render(request, Paths.edit_achievement,
                      {"form": form, "RosterId": roster_id})

    else:
        return render(request, Paths.home)
