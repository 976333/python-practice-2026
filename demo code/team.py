class Team:

    def __init__(self, team_id, name, short_name, home_city):
        self.team_id = team_id
        self.name = name
        self.short_name = short_name
        self.home_city = home_city
        self.players = []

    def add_player(self, player):
        # maximum 15 players
        if len(self.players) >= 15:
            print(f"{self.name} already has 15 players.")
            return False

        # check duplicate jersey number
        for i in self.players:
            # check the pass player jersey number with the existing player jersey number
            if i.jersey_number == player.jersey_number:
                print(f"Jersey number {player.jersey_number} is already used.")
                return False

        self.players.append(player)
        return True

    # method for the remove the player  
    def remove_player(self, player_id):
        for player in self.players:
            if player.player_id == player_id:
                self.players.remove(player)
                return player

        return None

    
    def find_player(self, name):
        for player in self.players:
            if player.name.lower() == name.lower():
                return player

        return None

    def players_by_role(self, role):
        result = []

        for player in self.players:
            if player.role.lower() == role.lower():
                result.append(player)

        return result

    def bowlers(self):
        result = []

        for player in self.players:
            if player.can_bowl():
                result.append(player)

        return result

    def is_ready_to_play(self):
        missing = []

        # At least 11 players
        if len(self.players) < 11:
            missing.append(
                f"Needs at least 11 players (has {len(self.players)})"
            )

        # At least 1 wicket-keeper
        wicket_keepers = self.players_by_role("Wicket-keeper")

        if len(wicket_keepers) < 1:
            missing.append("Needs at least 1 Wicket-keeper")

        # At least 5 players who can bowl
        bowlers = self.bowlers()

        if len(bowlers) < 5:
            missing.append(
                f"Needs at least 5 players who can bowl (has {len(bowlers)})"
            )

        if len(missing) == 0:
            return True, []

        return False, missing

    def show_squad(self):
        # Sort players by jersey number
        sorted_players = sorted(
            self.players,
            key=lambda player: player.jersey_number
        )

        print(f"\nSQUAD - {self.name} ({self.short_name}), {self.home_city}")
        print("-" * 60)
        print("No.  Name                 Role             Batting")
        print("-" * 60)

        for player in sorted_players:
            print(
                f"{player.jersey_number:<5}"
                f"{player.name:<21}"
                f"{player.role:<17}"
                f"{player.batting_style}"
            )

        wicket_keepers = len(self.players_by_role("Wicket-keeper"))
        bowlers = len(self.bowlers())

        ready, missing = self.is_ready_to_play()

        status = "Ready" if ready else "Not ready"

        print("-" * 60)
        print(
            f"Players: {len(self.players)} | "
            f"Wicket-keepers: {wicket_keepers} | "
            f"Can bowl: {bowlers} | "
            f"Status: {status}"
        )


        # -------------------------------------------------------------


ready, missing = team.is_ready_to_play()

if ready:
    print("Team is ready")
else:
    print("Team is NOT ready")
    for reason in missing:
        print("-", reason)