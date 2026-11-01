"""
owner name : chaitanya dusane

This file handles team data:
- Add player
- Remove player
- Find player
- Find player based on role
- Check bowler
- Check whether team is ready
"""

import json


class Team:

    def __init__(self, team_id, name, short_name, home_city):

        # ---------------- TEAM ID VALIDATION ----------------
        if not isinstance(team_id, int) or isinstance(team_id, bool):
            raise ValueError("Team ID must be a whole number.")

        if team_id <= 0:
            raise ValueError("Team ID must be greater than 0.")

        self.team_id = team_id

        # ---------------- TEAM NAME VALIDATION ----------------
        if not isinstance(name, str):
            raise ValueError("Team name must be text.")

        name = name.strip()

        if not name:
            raise ValueError("Team name cannot be empty.")

        if len(name) < 3 or len(name) > 50:
            raise ValueError(
                "Team name must be between 3 and 50 characters."
            )

        self.name = name

        # ---------------- SHORT NAME VALIDATION ----------------
        if not isinstance(short_name, str):
            raise ValueError("Short name must be text.")

        short_name = short_name.strip()

        if len(short_name) != 3:
            raise ValueError(
                "Short name must be exactly 3 capital letters."
            )

        if not short_name.isalpha() or not short_name.isupper():
            raise ValueError(
                "Short name must contain exactly 3 capital letters."
            )

        self.short_name = short_name

        # ---------------- HOME CITY VALIDATION ----------------
        if not isinstance(home_city, str):
            raise ValueError("Home city must be text.")

        home_city = home_city.strip()

        if not home_city:
            raise ValueError("Home city cannot be empty.")

        self.home_city = home_city

        # ---------------- PLAYERS ----------------
        self.players = []

    # =========================================================
    # CREATE TEAM FROM JSON
    # =========================================================

    @classmethod
    def from_json(cls, json_data):

        # JSON must be a string
        if not isinstance(json_data, str):
            raise ValueError("JSON data must be provided as a string.")

        # Convert JSON string into Python object
        try:
            data = json.loads(json_data)

        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data: {e}")

        # JSON must contain one team object
        if not isinstance(data, dict):
            raise ValueError(
                "Team JSON must contain an object."
            )

        # Check required fields
        required_fields = [
            "team_id",
            "team_name",
            "short_name",
            "home_city"
        ]

        for field in required_fields:
            if field not in data:
                raise ValueError(
                    f"Missing required field: {field}"
                )

        # Read data
        team_id = data["team_id"]
        name = data["team_name"]
        short_name = data["short_name"]
        home_city = data["home_city"]

        # Constructor performs all validation
        return cls(
            team_id,
            name,
            short_name,
            home_city
        )

    # =========================================================
    # ADD PLAYER
    # =========================================================

    def add_player(self, player):

        # Maximum 15 players
        if len(self.players) >= 15:
            print(f"{self.name} already has 15 players.")
            return False

        # Check duplicate jersey number
        for existing_player in self.players:

            if existing_player.jersey_number == player.jersey_number:
                print(
                    f"Jersey number {player.jersey_number} "
                    f"is already used."
                )
                return False

        self.players.append(player)

        return True

    # =========================================================
    # REMOVE PLAYER
    # =========================================================

    def remove_player(self, player_id):

        for player in self.players:

            if player.player_id == player_id:
                self.players.remove(player)
                return player

        return None

    # =========================================================
    # FIND PLAYER
    # =========================================================

    def find_player(self, name):

        for player in self.players:

            if player.name.lower() == name.lower():
                return player

        return None

    # =========================================================
    # FIND PLAYERS BY ROLE
    # =========================================================

    def players_by_role(self, role):

        result = []

        for player in self.players:

            if player.role.lower() == role.lower():
                result.append(player)

        return result

    # =========================================================
    # FIND BOWLERS
    # =========================================================

    def bowlers(self):

        result = []

        for player in self.players:

            if player.can_bowl():
                result.append(player)

        return result

    # =========================================================
    # CHECK TEAM READY
    # =========================================================

    def is_ready_to_play(self):

        missing = []

        # At least 11 players
        if len(self.players) < 11:

            missing.append(
                f"Needs at least 11 players "
                f"(has {len(self.players)})"
            )

        # At least 1 wicket keeper
        wicket_keepers = self.players_by_role(
            "Wicket-keeper"
        )

        if len(wicket_keepers) < 1:

            missing.append(
                "Needs at least 1 Wicket-keeper"
            )

        # At least 5 players who can bowl
        bowlers = self.bowlers()

        if len(bowlers) < 5:

            missing.append(
                f"Needs at least 5 players who can bowl "
                f"(has {len(bowlers)})"
            )

        # Team ready
        if len(missing) == 0:
            return True, []

        return False, missing

    # =========================================================
    # SHOW SQUAD
    # =========================================================

    def show_squad(self):

        sorted_players = sorted(
            self.players,
            key=lambda player: player.jersey_number
        )

        print(
            f"\nSquad - {self.name} "
            f"({self.short_name}), {self.home_city}"
        )

        print("-" * 60)

        print(
            "No.  Name                 Role             Batting"
        )

        print("-" * 60)

        for player in sorted_players:

            print(
                f"{player.jersey_number:<5}"
                f"{player.name:<21}"
                f"{player.role:<17}"
                f"{player.batting_style}"
            )

        wicket_keepers = len(
            self.players_by_role("Wicket-keeper")
        )

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







        # --------------------------------------------------------------------



        """owner name : chaitanya dusane
this file for the team data handle 
- Add player
- Remove player 
- Find player
- Find based on role 
- Check bowler
- check team is ready 
"""
import json

class Team():

    def __init__(self,team_id, name, short_name,home_city):
        # Validate team ID
        if not isinstance(team_id, int):
            raise ValueError("Team ID must be a whole number.")
        self.team_id = team_id

        # Validate team name
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Team name cannot be empty.")

        if len(name.strip()) < 3 or len(name.strip()) > 50:
            raise ValueError("Team name must be between 3 and 50 characters.")

        self.name = name.strip()

        # Validate short name
        if not isinstance(short_name, str):
            raise ValueError("Short name must be text.")

        if len(short_name) != 3:
            raise ValueError(
                "Short name must be exactly 3 capital letters."
            )

        if not short_name.isupper() or not short_name.isalpha():
            raise ValueError(
                "Short name must be exactly 3 capital letters."
            )
        
        self.short_name= short_name

        # Validate home city
        if not isinstance(home_city, str) or not home_city.strip():
            raise ValueError("Home city cannot be empty.")
        
        self.home_city =home_city.strip()

        #store players
        self.players = []



    @classmethod
    def from_json(cls, json_data):
        try:
            data = json.loads(json_data)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data.")

        if not isinstance(data, dict):
            raise ValueError("Team JSON must contain an object.")

        team_id = data.get("team_id")
        name = data.get("team_name")
        short_name = data.get("short_name")
        home_city = data.get("home_city")

        return cls(
            team_id,
            name,
            short_name,
            home_city
        )


    
    def add_player(self,player):
        # maximum 15 players
        if len(self.players)>=15:
            print(f"{self.name} already has 15 players ")
            return False
        # check the pass player jersey number with the existing player jersey number
        for i in self.players:
            if i.jersey_number == player.jersey_number:
                print(f"jersey number {player.jersey_number}is already used.")
                return False

        self.players.append(player)
        return True

    # method for remove player
    def remove_player(self,player_id):
        for player in self.players:
            if player.player_id== player_id:
                self.players.remove(player)
                return player

        return None

    # method for find the player 
    def find_player(self,name):
        for player in self.players:
            if player.name.lower()==name.lower():
                return player
        return None

    # return player role
    def players_by_role(self,role):
        result = [] 

        for player in self.players:
            if player.role.lower()==role.lower():
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
        
        # at least 11 players
        if len(self.players) < 11:
            missing.append(f"Needs at least 11 players (has {len(self.players)})")
        
        # at least 1 wicket-keeper
        wicket_keepers = self.players_by_role("Wicket-keeper")
        
        if len(wicket_keepers) < 1:
            missing.append("Needs at least 1 Wicket-keeper")
        
        # At least 5 players who can bowl
        bowlers = self.bowlers()
        
        if len(bowlers) < 5:
            missing.append(f"Needs at least 5 players who can bowl (has {len(bowlers)})")
        
        if len(missing) == 0:
            return True, []
        
        return False, missing
        

    def show_squad(self):
        sorted_players =sorted(self.players,key =lambda player:player.jersey_number)

        print(f"\n squad - { self.name} ({self.short_name}),{self.home_city}")
        print("-"*60)
        print("no. name                role             Batting")
        print("-"*60)

        for player in sorted_players:
            print(
                f"{player.jersey_number:<5}"
                f"{player.name:<21}"
                f"{player.role:<17}"
                f"{player.batting_style}"
            )

        wicket_keepers = len(self.players_by_role("Wicket-keeper"))
        bowlers = len(self.bowlers())

        ready,missing =self.is_ready_to_play()

        status = "ready" if ready else "Not ready"

        print ("-"*60)
        print(
            f"Players: {len(self.players)} | "
            f"Wicket-keepers: {wicket_keepers} | "
            f"Can bowl: {bowlers} | "
            f"Status: {status}"
        )

# team1 = Team(1, "", "INF", "Pune")
# print(team1.name)
# print(team1.short_name)
# print(team1.home_city)




# demo data for test the method 
# hear check the team all constrainsts are match or not 
# ready, missing = Team("[{'team_id': 3, 'team_name': 'ATLAX', 'short_name': 'ATL', 'home_city': 'pune', 'created_on': datetime.datetime(2026, 10, 28, 16, 15, 44)}, {'team_id': 6, 'team_name': 'Meow', 'short_name': 'MWO', 'home_city': 'Pune', 'created_on': datetime.datetime(2026, 10, 28, 16, 52, 23)}, {'team_id': 7, 'team_name': 'df', 'short_name': 're', 'home_city': 'Mumbai', 'created_on': datetime.datetime(2026, 10, 28, 17, 44, 47)}]").is_ready_to_play()

# if ready:
#     print("team is ready")
# else:
#     print("team is not ready")
# for reason in missing:
#     print("-",reason)



#  json_data = {
     
#  }


# data = json.loads()






