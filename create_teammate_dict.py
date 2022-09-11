import os
import csv
import json

teams = [
"buf", "nwe", "mia", "nyj", "oti", "clt", "htx", "jax", "cin", "pit", "cle", "rav", 
"kan", "rai", "sdg", "den", "dal", "phi", "was", "nyg", "tam", "nor", "atl", "car", 
"gnb", "min", "chi", "det", "ram", "crd", "sfo", "sea"]


class PlayerTeamDict:
	def __init__(self):
		self.teammate_dict = {x : set() for x in range(11661)}
		
	def add_teammate(self, player1_id, player2_id):
		self.teammate_dict[player1_id].add(player2_id)
		self.teammate_dict[player2_id].add(player1_id)

	def set_teammates_from_roster(self, id_roster):
		#print(id_roster)
		for p1 in id_roster:
			for p2 in id_roster:
				if p1 != p2:
					self.add_teammate(p1, p2)

	def json_preprocess(self):
		return {x : list(y) for x, y in self.teammate_dict.items()}

def get_yr(team):
	if team == "htx":
		return 2002
	if team == "cle":
		return 1999
	return 1996


data = json.load(open('player_lookup_table_alphabetized.json'))

name_number_dict = {v: int(k) for k, v in data.items()}
#print(name_number_dict)

team_dict = PlayerTeamDict()

for team in teams:
	for yr in range(get_yr(team), 2023):
		with open('{}{}.csv'.format(team, yr)) as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			players = [name_number_dict[row[1]] for row in reader if row[1] != "Player" if row[1] != "Team Total"][1:]
			team_dict.set_teammates_from_roster(players)


with open("player_teammates.json", "w+") as outfile:
    json.dump(team_dict.json_preprocess(), outfile)


			


