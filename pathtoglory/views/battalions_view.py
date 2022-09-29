from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from ..models import Battalions
from ..forms import BattalionsForm
from ..helpers.paths import Paths


@csrf_protect
def battalions(request, vault_id):
    form = BattalionsForm()

    if request.method == 'POST':
        update_request = request.POST.copy()
        update_request.update({'Vault_Id': vault_id})
        form = BattalionsForm(update_request)
        if form.is_valid():
            form.save()
            form = BattalionsForm()

    battalion = list(Battalions.objects.filter(Vault_Id=vault_id))

    return render(request, Paths.battalions, {"form": form, "Vault_Id": vault_id,
                                              "vault_item": battalion})


@csrf_protect
def edit_battalion(request, battalion_id):
    battalion = Battalions.objects.get(id=battalion_id)
    form = BattalionsForm(instance=battalion)

    if request.method == 'POST':
        instance = get_object_or_404(Battalions, id=battalion_id)
        form = BattalionsForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('battalions', vault_id=battalion.Vault_Id.id)

    return render(request, Paths.edit_battalions, {"form": form})


@csrf_protect
def delete_battalion(request, battalion_id):
    battalion = get_object_or_404(Battalions, id=battalion_id)
    vault_id = battalion.Vault_Id.id

    if request.method == 'GET':
        battalion.delete()

    return redirect('battalions', vault_id=vault_id)
