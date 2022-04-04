class Team:
    def __init__(self, input_team_name, input_players_list, input_coach):
        self.name = input_team_name
        self.players = input_players_list
        self.coach = input_coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, find_player):
        found_player = False
        for player in self.players:
            if find_player == player:
                found_player = True
        return found_player

    def play_game(self, win_game):
        if win_game:
            self.points += 3
        else:
            return self.points

