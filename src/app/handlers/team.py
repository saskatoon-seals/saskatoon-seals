import json
from app.handlers import BaseHandler
from app.models.player import PlayerModel


class TeamHandler(BaseHandler):
    def get(self):
        """
        :return: all the players of the team.
        """
        # team = PlayerModel.get_all_players()
        # context = {
        #     'players': [player.to_dict(to_json_str=True) for player in team]
        # }
        context = {}
        return self.render_response('team.html', **context)