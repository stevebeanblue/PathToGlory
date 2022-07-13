from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import PathToGloryGroup, Roster, QuestLog, Stronghold, Achievements
from .forms import CreateRosterForm, QuestLogForm, StrongholdForm, AchievementsForm
from .helpers.paths import Paths


def home(request):
    if request.method == 'GET':
        return render(request, Paths.home, {"PathToGloryGroup": list(PathToGloryGroup.objects.all())})


def grouprosters(request, group_id):
    if request.method == 'GET':
        return render(request, Paths.group_rosters,
                      {"Rosters": list(Roster.objects.filter(Group_id=group_id))})


def createroster(request):
    if request.method == 'GET':
        form = CreateRosterForm()
        return render(request, Paths.create_roster, {"form": form})
    else:
        update_request = request.POST.copy()
        update_request.update({'User_id': request.user.id, 'DateCreated': datetime.now(), 'PlayerName': request.user})
        form = CreateRosterForm(update_request)
        if form.is_valid():
            form.save()
        else:
            return render(request, Paths.create_roster, {"form": form})
        return render(request, Paths.home, {"PathToGloryGroup": list(PathToGloryGroup.objects.all())})


def editroster(request, roster_id):
    try:
        roster = Roster.objects.get(pk=int(roster_id))
    except Roster.DoesNotExist:
        return home(request)

    if not roster or request.user.id != roster.User_id:
        return home(request)

    if request.method == 'GET':
        form = CreateRosterForm(instance=roster)
        return render(request, Paths.edit_roster, {"form": form, "RosterId": roster_id})
    else:
        form = CreateRosterForm(request.POST, instance=roster)
        form.save()
        return render(request, Paths.group_rosters,
                      {"Rosters": list(Roster.objects.filter(Group_id=roster.Group_id))})


def createquestlog(request, roster_id):
    form = QuestLogForm()
    quests = list(QuestLog.objects.filter(RosterId=roster_id))

    if request.method == 'GET':
        return render(request,
                      Paths.create_quest_log,
                      {"form": form,
                       "RosterId": roster_id,
                       "quests": quests})
    else:
        update_request = request.POST.copy()
        update_request.update({'RosterId': roster_id})
        form = QuestLogForm(update_request)
        if form.is_valid():
            form.save()
            form = QuestLogForm()
            quests = list(QuestLog.objects.filter(RosterId=roster_id))

    return render(request, Paths.create_quest_log, {"form": form, "RosterId": roster_id, "quests": quests})


def edit_quest_log(request, quest_id):
    quest = QuestLog.objects.get(pk=quest_id)
    form = QuestLogForm(instance=quest)

    if request.method == 'POST':
        instance = get_object_or_404(QuestLog, id=quest_id)
        form = QuestLogForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('createquestlog', roster_id=quest.RosterId)

    return render(request, Paths.edit_quest_log,
                  {"form": form, "RosterId": quest.RosterId})


def delete_quest_log(request, quest_id):
    quest = QuestLog.objects.get(pk=quest_id)
    roster_id = quest.RosterId

    if request.method == 'GET':
        quest.delete()

    return redirect('createquestlog', roster_id=roster_id)


def createstronghold(request, roster_id):
    form = StrongholdForm()

    if request.method == 'POST':
        update_request = request.POST.copy()
        update_request.update({'RosterId': roster_id})
        form = StrongholdForm(update_request)
        if form.is_valid():
            form.save()
            form = StrongholdForm()

    strongholds = list(Stronghold.objects.filter(RosterId=roster_id))

    return render(request, Paths.create_stronghold, {"form": form, "RosterId": roster_id, "strongholds": strongholds})


def edit_stronghold(request, stronghold_id):
    stronghold = Stronghold.objects.get(pk=stronghold_id)
    form = StrongholdForm(instance=stronghold)

    if request.method == 'POST':
        instance = get_object_or_404(Stronghold, id=stronghold_id)
        form = StrongholdForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('createstronghold', roster_id=stronghold.RosterId)

    return render(request, Paths.edit_stronghold,
                  {"form": form, "RosterId": stronghold.RosterId})


def delete_stronghold(request, stronghold_id):
    stronghold = Stronghold.objects.get(pk=stronghold_id)
    roster_id = stronghold.RosterId

    if request.method == 'GET':
        stronghold.delete()

    return redirect('createstronghold', roster_id)


def create_achievements(request, roster_id):
    instance = Achievements.get_achievement(roster_id)

    if instance:
        if len(instance) > 1:
            return redirect('home')
        form = AchievementsForm(instance=instance[0])
    else:
        form = AchievementsForm()

    if request.method == 'POST':

        achievement = Achievements.get_achievement(roster_id)

        if achievement:
            form = AchievementsForm(request.POST or None, instance=achievement[0])
            update_request = request.POST.copy()
            update_request.update({'RosterId': roster_id})

        if form.is_valid():
            form.save()

    return render(request, Paths.create_achievement,
                  {"form": form, "RosterId": roster_id})
