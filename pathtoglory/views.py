from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import PathToGloryGroup, Roster, QuestLog, Stronghold, Achievements, BonusArtifactsOfPower, TheVault
from .forms import CreateRosterForm, QuestLogForm, StrongholdForm, AchievementsForm, BonusArtifactsOfPowerForm
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
        update_request.update({'User_id': request.user.id, 'DateCreated': datetime.now(), 'PlayerName': request.user,
                               'Group_id_as_int': request.POST.get("Group_id")})
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

    return render(request, Paths.view_achievement, {"form": form})


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
            return redirect('createstronghold', roster_id=stronghold.RosterId)

    return render(request, Paths.edit_achievement,
                  {"form": form, "RosterId": achievement.RosterId})


def bonus_artifacts_of_power(request, roster_id):
    form = BonusArtifactsOfPowerForm()

    if request.method == 'POST':
        update_request = request.POST.copy()
        update_request.update({'RosterId': roster_id})
        form = BonusArtifactsOfPowerForm(update_request)
        if form.is_valid():
            form.save()
            form = BonusArtifactsOfPowerForm()

    powers = list(BonusArtifactsOfPower.objects.filter(RosterId=roster_id))

    return render(request, Paths.bonusartifactsofpower, {"form": form, "RosterId": roster_id, "powers": powers})


def edit_bonus_artifacts_of_power(request, power_id):
    power = BonusArtifactsOfPower.objects.get(pk=power_id)
    form = BonusArtifactsOfPowerForm(instance=power)

    if request.method == 'POST':
        instance = get_object_or_404(BonusArtifactsOfPower, id=power_id)
        form = BonusArtifactsOfPowerForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('bonus_artifacts_of_power', roster_id=power.RosterId)

    return render(request, Paths.edit_stronghold,
                  {"form": form, "RosterId": power.RosterId})


def delete_bonus_artifacts_of_power(request, power_id):
    power = BonusArtifactsOfPower.objects.get(pk=power_id)
    roster_id = power.RosterId

    if request.method == 'GET':
        power.delete()

    return redirect('bonus_artifacts_of_power', roster_id)


def the_vault(request, roster_id):
    vault = TheVault.objects.get_or_create(RosterId=roster_id)
    return render(request, Paths.the_vault, {"vault": vault})
