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
    bonus_artifacts_of_power_view, the_vault_view, bonus_unique_enhancement_view, bonus_spells_view, \
    bonus_prayers_view, endless_spells_and_invocations_view, battalions_view, order_of_battle_view, \
    warlord_view, hero_view, unit_view, notes_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),  # new
    path("accounts/", include("django.contrib.auth.urls")),
    path("", home_view.home, name="home"),
    # region vault
    path("thevault/<int:roster_id>/", the_vault_view.the_vault, name="thevault"),
    path("editvault/<int:vault_id>/", the_vault_view.edit_vault, name="editvault"),
    path("createvault/<int:roster_id>/", the_vault_view.create_vault, name="createvault"),
    path("deletevault/<int:roster_id>/", the_vault_view.delete_vault, name="deletevault"),
    # endregion
    # region roster
    path("grouprosters/<int:group_id>/", rosters_view.grouprosters, name="grouprosters"),
    path("editroster/<int:roster_id>/", rosters_view.editroster, name="editroster"),
    path("createroster/", rosters_view.createroster, name="createroster"),
    path("myrosters/", rosters_view.my_rosters, name="my_rosters"),
    path("deleteroster/<int:roster_id>", rosters_view.delete_roster, name="delete_roster"),
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
    path("bonusartifactsofpower/<int:vault_id>/", bonus_artifacts_of_power_view.bonus_artifacts_of_power,
         name="bonusartifactsofpower"),
    path("editbonusartifactsofpower/<int:power_id>", bonus_artifacts_of_power_view.edit_bonus_artifacts_of_power,
         name="editartifactofpower"),
    path("deleteartifactofpower/<int:power_id>/",
         bonus_artifacts_of_power_view.delete_bonus_artifacts_of_power, name="deleteartifactofpower"),
    # endregion
    # region bonus unique enhancements
    path("bonusuniqueenhancement/<int:vault_id>", bonus_unique_enhancement_view.bonus_unique_enhancement,
         name="bonus_unique_enhancement"),
    path("editbonusuniqueenhancement/<int:unique_id>", bonus_unique_enhancement_view.edit_bonus_unique_enhancement,
         name="edit_bonus_unique_enhancement"),
    path("deletebonusuniqueenhancement/<int:unique_id>",
         bonus_unique_enhancement_view.delete_bonus_unique_enhancement, name="delete_bonus_unique_enhancement"),
    # endregion
    # region bonus spells
    path("bonusspell/<int:vault_id>", bonus_spells_view.bonus_spell, name="bonus_spells"),
    path("editbonusspell/<int:spell_id>", bonus_spells_view.edit_bonus_spell, name="edit_bonus_spell"),
    path("deletebonusspell/<int:spell_id>", bonus_spells_view.delete_bonus_spell, name="delete_bonus_spell"),
    # endregion
    # region bonus prayers
    path("bonusprayers/<int:vault_id>", bonus_prayers_view.bonus_prayers, name="bonus_prayers"),
    path("editbonusprayers/<int:prayer_id>", bonus_prayers_view.edit_bonus_prayers, name="edit_bonus_prayers"),
    path("deletebonusprayers/<int:prayer_id>", bonus_prayers_view.delete_bonus_prayers, name="delete_bonus_prayers"),
    # endregion
    # region endless spells and invocations
    path("endlessspellsandinvocations/<int:vault_id>", \
         endless_spells_and_invocations_view.endless_spells_and_invocations, name="endless_spells_and_invocations"),
    path("editendlessspellsandinvocations/<int:endless_id>", \
         endless_spells_and_invocations_view.edit_endless_spells_and_invocations, \
         name="edit_endless_spells_and_invocations"),
    path("deleteendlessspellsandinvocations/<int:endless_id>", \
         endless_spells_and_invocations_view.delete_endless_spells_and_invocations, \
         name="delete_endless_spells_and_invocations"),
    # endregion
    # region battalions
    path("battalions/<int:vault_id>", battalions_view.battalions, name="battalions"),
    path("editbattalion/<int:battalion_id>", battalions_view.edit_battalion, name="edit_battalion"),
    path("deletebattalion/<int:battalion_id>", battalions_view.delete_battalion, name="delete_battalion"),
    # endregion
    # region order of battle
    path("orderofbattle/<int:roster_id>", order_of_battle_view.order_of_battle, name="order_of_battle"),
    path("editorderofbattle/<int:order_of_battle_id>", order_of_battle_view.edit_order_of_battle, \
         name="edit_order_of_battle"),
    path("createorderofbattle/<int:roster_id>", order_of_battle_view.create_order_of_battle, \
         name="create_order_of_battle"),
    path("order_of_battle_summary/<int:roster_id>", order_of_battle_view.order_of_battle_summary, \
         name="order_of_battle_summary"),
    # endregion
    # region warlord
    path("warlord/<int:roster_id>", warlord_view.warlord, name="warlord"),
    path("editwarlord/<int:roster_id>", warlord_view.edit_warlord, name="edit_warlord"),
    path("deletewarlord/<int:roster_id>", warlord_view.delete_warlord, name="delete_warlord"),
    path("createwarlord/<int:roster_id>", warlord_view.create_warlord, name="create_warlord"),
    # endregion
    # region hero
    path("hero/<int:roster_id>", hero_view.hero, name="hero"),
    path("edithero/<int:hero_id>", hero_view.edit_hero, name="edit_hero"),
    path("deletehero/<int:hero_id>", hero_view.delete_hero, name="delete_hero"),
    # endregion
    # region units
    path("unit/<int:roster_id>", unit_view.unit, name="unit"),
    path("editunit/<int:unit_id>", unit_view.edit_unit, name="edit_unit"),
    path("deleteunit/<int:unit_id>", unit_view.delete_unit, name="delete_unit"),
    # endregion
    # region notes
    path("notes/<int:roster_id>", notes_view.notes, name="notes"),
    path("edit_note/<int:note_id>", notes_view.edit_note, name="edit"),
    path("delete_note/<int:note_id>", notes_view.delete_note, name="delete"),
    path("create/<int:roster_id>", notes_view.create_note, name="create")
    # end region
]
