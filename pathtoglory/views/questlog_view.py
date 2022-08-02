from django.shortcuts import render, redirect, get_object_or_404
from ..models import QuestLog
from ..forms import QuestLogForm
from ..helpers.paths import Paths


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