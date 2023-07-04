from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from ..helpers import user_by_roster_id
from ..models import QuestLog
from ..forms import QuestLogForm
from ..helpers.paths import Paths


@csrf_protect
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
        user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)
        if user_id == request.user.id:
            update_request = request.POST.copy()
            update_request.update({'RosterId': roster_id})
            form = QuestLogForm(update_request)
            if form.is_valid():
                form.save()
                form = QuestLogForm()
                quests = list(QuestLog.objects.filter(RosterId=roster_id))

    return render(request, Paths.create_quest_log, {"form": form, "RosterId": roster_id, "quests": quests})


@login_required
@csrf_protect
def edit_quest_log(request, quest_id):
    quest = get_object_or_404(QuestLog, id=quest_id)
    user_id = user_by_roster_id.get_user_id_by_roster_id(quest.Roster_Id)
    if user_id == request.user.id:
        form = QuestLogForm(instance=quest)
        if request.method == 'POST':
            form = QuestLogForm(request.POST or None, instance=quest)
            if form.is_valid():
                form.save()
                return redirect('createquestlog', roster_id=quest.RosterId)

        return render(request, Paths.edit_quest_log,
                      {"form": form, "RosterId": quest.RosterId})


@login_required
@csrf_protect
def delete_quest_log(request, quest_id):
    quest = get_object_or_404(QuestLog, id=quest_id)
    user_id = user_by_roster_id.get_user_id_by_roster_id(quest.Roster_Id)

    if request.method == 'GET' and user_id == request.user.id:
        quest.delete()

    return redirect('createquestlog', roster_id=quest.RosterId)