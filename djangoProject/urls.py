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
from pathtoglory.views \
    import achievements_view, home_view, rosters_view, questlog_view, stronghold_view, \
            bonus_artifacts_of_power_view, the_vault_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),  # new
    path("accounts/", include("django.contrib.auth.urls")),
    path("", home_view.home, name="home"),
    path("thevault/<int:roster_id>/", the_vault_view.the_vault, name="thevault"),
    # region roster
    path("grouprosters/<int:group_id>/", rosters_view.grouprosters, name="grouprosters"),
    path("editroster/<int:roster_id>", rosters_view.editroster, name="editroster"),
    path("createroster/", rosters_view.createroster, name="createroster"),
    # endregion
    # region quests
    path("createquestlog/<int:roster_id>/", questlog_view.createquestlog, name="createquestlog"),
    path("editquestlog/<int:quest_id>/", questlog_view.edit_quest_log, name="editquestlog"),
    path("deletequestlog/<int:quest_id>/", questlog_view.delete_quest_log, name="deletequestlog"),
    # endregion
    # region strongholds
    path("createstronghold/<int:roster_id>", stronghold_view.createstronghold, name="createstronghold"),
    path("editstronghold/<int:stronghold_id>/", stronghold_view.edit_stronghold, name="editstronghold"),
    path("deletestronghold/<int:stronghold_id>/",
         stronghold_view.delete_stronghold, name="deletestronghold"),
    # endregion
    # region achievements
    path("achievements/<int:roster_id>", achievements_view.create_achievements, name="createachievements"),
    path("achievement/<int:roster_id>", achievements_view.view_achievement, name="viewachievement"),
    path("editachievements/<int:roster_id>", achievements_view.edit_achievements, name="editachievements"),
    # endregion
    # region bonus artifacts of power
    path("bonusartifactsofpower/<int:roster_id>", bonus_artifacts_of_power_view.bonus_artifacts_of_power, name="artifactofpower"),
    path("editbonusartifactsofpower/<int:power_id>", bonus_artifacts_of_power_view.edit_bonus_artifacts_of_power, name="editartifactofpower"),
    path("deletebonusartifactsofpower/<int:power_id>/",
         bonus_artifacts_of_power_view.delete_bonus_artifacts_of_power, name="deletebonusartifactsofpower")
    # endregion
]
