from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect

from ..helpers import user_by_roster_id
from ..models import Notes
from ..forms import NotesForm
from ..helpers.paths import Paths


@csrf_protect
@login_required
def notes(request, roster_id):
    user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)

    if user_id == request.user.id and request.method == 'GET':
        general_notes = list(Notes.objects.filter(Roster_Id=roster_id, general=True))
        print(general_notes)
        hero_phase_notes = list(Notes.objects.filter(Roster_Id=roster_id, hero_phase=True))
        movement_phase_notes = list(Notes.objects.filter(Roster_Id=roster_id, movement_phase=True))
        shooting_phase_notes = list(Notes.objects.filter(Roster_Id=roster_id, shooting_phase=True))
        combat_phase_notes = list(Notes.objects.filter(Roster_Id=roster_id, combat_phase=True))

    return render(request, Paths.notes, {"general_notes": general_notes, "hero_phase_notes": hero_phase_notes,
                                         "movement_phase_notes": movement_phase_notes,
                                         "shooting_phase_notes": shooting_phase_notes,
                                         "combat_phase_notes": combat_phase_notes, "user_id": user_id,
                                         "roster_id": roster_id})


def create_note(request, roster_id):
    user_id = user_by_roster_id.get_user_id_by_roster_id(roster_id)
    edit = False
    if user_id == request.user.id:
        if request.method == 'GET':
            form = NotesForm
            if hasattr(NotesForm, 'note'):
                print("Note exists")
            return render(request, Paths.edit_note, {"form": form, "edit": edit})
        else:
            update_request = request.POST.copy()
            update_request.update({'Roster_Id': roster_id})
            form = NotesForm(update_request)
            if form.is_valid():
                form.save()
                return redirect('notes', roster_id=roster_id)
    else:
        return redirect('notes', roster_id=roster_id)



@login_required
@csrf_protect
def edit_note(request, note_id):
    note = get_object_or_404(Notes, id=note_id)
    user_id = user_by_roster_id.get_user_id_by_roster_id(note.Roster_Id)
    form = NotesForm(instance=note)
    edit = True
    if user_id == request.user.id:
        if request.method == 'POST':
            instance = get_object_or_404(Notes, id=note_id)
            form = NotesForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('notes', roster_id=instance.Roster_Id)

        return render(request, Paths.edit_note, {"form": form, "edit": edit})
    else:
        if hasattr(form, 'note'):
            print("a note")
        return render(request, Paths.edit_note, {"form": form, "Roster_Id": note.Roster_Id, "edit": edit})


@login_required
@csrf_protect
def delete_note(request, note_id):
    note = get_object_or_404(Notes, id=note_id)
    user_id = user_by_roster_id.get_user_id_by_roster_id(note.Roster_Id)
    roster_id = note.Roster_Id

    if user_id == request.user.id:
        if request.method == 'GET':
            note.delete()

    return redirect('notes', roster_id=roster_id)
