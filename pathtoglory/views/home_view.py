from django.shortcuts import render
from ..models import PathToGloryGroup
from ..helpers.paths import Paths


def home(request):
    if request.method == 'GET':
        return render(request, Paths.home, {"PathToGloryGroup": list(PathToGloryGroup.objects.all())})