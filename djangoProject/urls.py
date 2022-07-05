"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pathtoglory import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),  # new
    path("accounts/", include("django.contrib.auth.urls")),
    path("", views.home, name="home"),
    path("grouprosters/<int:group_id>", views.grouprosters, name="grouprosters"),
    path("editroster/<int:roster_id>", views.editroster, name="editroster"),
    path("createroster/", views.createroster, name="createroster"),
    path("createquestlog/<int:roster_id>", views.createquestlog, name="createquestlog"),
    path("editquestlog/<int:quest_id>/<int:roster_id>", views.edit_quest_log, name="editquestlog"),
    path("deletequestlog/<int:quest_id>/<int:roster_id>", views.delete_quest_log, name="deletequestlog"),
]