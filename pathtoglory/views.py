from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import PathToGloryGroup, Roster, QuestLog
from .forms import CreateRosterForm, QuestLogForm
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
        # add validation to only be able to have one quest per roster
        update_request = request.POST.copy()
        update_request.update({'RosterId': roster_id})
        form = QuestLogForm(update_request)
        if form.is_valid():
            form.save()
            form = QuestLogForm()
            quests = list(QuestLog.objects.filter(RosterId=roster_id))

    return render(request, Paths.create_quest_log, {"form": form, "RosterId": roster_id, "quests": quests})


def edit_quest_log(request, quest_id, roster_id):
    html_file_path = Paths.create_quest_log
    quest = QuestLog.objects.get(pk=quest_id)
    form = QuestLogForm(instance=quest)
    quests = list(QuestLog.objects.filter(RosterId=roster_id))
    is_edit = "True"

    if request.method == 'POST':
        instance = get_object_or_404(QuestLog, id=quest_id)
        form = QuestLogForm(request.POST or None, instance=instance)
        if form.is_valid():
            is_edit = "False"
            form.save()
            form = CreateRosterForm()
            html_file_path = Paths.edit_roster

    return render(request, html_file_path,
                  {"form": form, "RosterId": roster_id, "quests": quests, "isEdit": is_edit})


def delete_quest_log(request, quest_id, roster_id):
    if request.method == 'GET':
        QuestLog.objects.filter(pk=quest_id).delete()

    return render(request, Paths.edit_roster, {"RosterId": roster_id, })



