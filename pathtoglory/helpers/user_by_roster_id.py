from ..models import Roster

def get_user_id_by_roster_id(roster_id):

    roster = Roster.objects.get(pk=roster_id)
    return roster.User_id