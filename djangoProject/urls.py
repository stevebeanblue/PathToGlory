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
    path("thevault/<int:roster_id>/", views.the_vault, name="thevault"),
    # region roster
    path("grouprosters/<int:group_id>/", views.grouprosters, name="grouprosters"),
    path("editroster/<int:roster_id>", views.editroster, name="editroster"),
    path("createroster/", views.createroster, name="createroster"),
    # endregion
    # region quests
    path("createquestlog/<int:roster_id>/", views.createquestlog, name="createquestlog"),
    path("editquestlog/<int:quest_id>/", views.edit_quest_log, name="editquestlog"),
    path("deletequestlog/<int:quest_id>/", views.delete_quest_log, name="deletequestlog"),
    # endregion
    # region strongholds
    path("createstronghold/<int:roster_id>", views.createstronghold, name="createstronghold"),
    path("editstronghold/<int:stronghold_id>/", views.edit_stronghold, name="editstronghold"),
    path("deletestronghold/<int:stronghold_id>/",
         views.delete_stronghold, name="deletestronghold"),
    # endregion
    # region achievements
    path("achievements/<int:roster_id>", views.create_achievements, name="createachievements"),
    path("achievement/<int:roster_id>", views.view_achievement, name="viewachievement"),
    path("editachievements/<int:roster_id>", views.edit_achievements, name="editachievements"),
    # endregion
    # region bonus artifacts of power
    path("bonusartifactsofpower/<int:roster_id>", views.bonus_artifacts_of_power, name="artifactofpower"),
    path("editbonusartifactsofpower/<int:power_id>", views.edit_bonus_artifacts_of_power, name="editartifactofpower"),
    path("deletebonusartifactsofpower/<int:power_id>/",
         views.delete_bonus_artifacts_of_power, name="deletebonusartifactsofpower")
    # endregion
]
