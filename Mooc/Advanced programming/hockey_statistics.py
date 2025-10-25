import json

class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games

    def __str__(self):
        return f"{self.name:<20} {self.team:>3} {self.goals:>3} + {self.assists:>2} = {self.goals + self.assists:>3}"

class App:
    def __init__(self):
        self.data = None
        self.filename = ""
        self.players = []

    def search_player(self):
        name = input("name: ")
        for player in self.players:
            if player.name == name:
                print(player)

    def search_teams(self):
        teams = sorted(set(player.team for player in self.players))
        for team in teams:
            print(team)

    def search_countries(self):
        countries = sorted(set(player.nationality for player in self.players))
        for country in countries:
            print(country)

    def team_stats(self):
        team_name = input("team: ")
        team_players = [player for player in self.players if player.team == team_name]
        team_players = sorted(team_players, key=lambda player: player.goals + player.assists, reverse=True)
        for player in team_players:
            print(player)

    def country_stats(self):
        country_name = input("country: ")
        country_players = [player for player in self.players if player.nationality == country_name]
        country_players = sorted(country_players, key=lambda player: player.goals + player.assists, reverse=True)
        for player in country_players:
            print(player)

    def most_points(self):
        amount = int(input("how many: "))
        most = sorted(self.players, key=lambda player: (-(player.goals + player.assists), player.goals))
        for i in range(min(amount, len(most))):
            print(most[i])

    def most_goals(self):
        amount = int(input("how many: "))
        most = sorted(self.players, key=lambda player: (-player.goals, player.games))
        for i in range(min(amount, len(most))):
            print(most[i])

    def execute(self):
        self.filename = input("file name: ")
        try:
            with open(self.filename) as file:
                self.data = json.load(file)
                for item in self.data:
                    player = Player(**item)
                    self.players.append(player)
        except FileNotFoundError:
            return
        print(f"read the data of {len(self.players)} players")

        print("commands:")
        while True:
            print("0 quit")
            print("1 search for player")
            print("2 teams")
            print("3 countries")
            print("4 players in team")
            print("5 players from country")
            print("6 most points")
            print("7 most goals")
            command = int(input("command: "))

            if command == 0:
                break
            elif command == 1:
                self.search_player()
            elif command == 2:
                self.search_teams()
            elif command == 3:
                self.search_countries()
            elif command == 4:
                self.team_stats()
            elif command == 5:
                self.country_stats()
            elif command == 6:
                self.most_points()
            elif command == 7:
                self.most_goals()


app = App()
app.execute()
