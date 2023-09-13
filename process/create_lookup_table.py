import os
import csv
import json
import re

MOST_RECENT_YEAR = 2024

teams = [
"buf", "nwe", "mia", "nyj", "oti", "clt", "htx", "jax", "cin", "pit", "cle", "rav", 
"kan", "rai", "sdg", "den", "dal", "phi", "was", "nyg", "tam", "nor", "atl", "car", 
"gnb", "min", "chi", "det", "ram", "crd", "sfo", "sea"]


class PlayerLookupDict:
	def __init__(self):
		self.lookup_dict = set()
		self.players = []

	def add_or_ignore(self, player):
		if player not in self.lookup_dict:
			self.lookup_dict.add(player)
			self.players.append(player)

def get_yr(team):
	if team == "htx":
		return 2002
	if team == "cle":
		return 1999
	return 1996


pld = PlayerLookupDict()

data_path = "../raw-data"

for team in teams:
	for yr in range(get_yr(team), MOST_RECENT_YEAR):
		with open(f'{data_path}/{team}{yr}.csv') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			for row in reader:
				if row[1] == "Player" or row[1] == "Team Total":
					continue
				
				pld.add_or_ignore(row[1])

pld.players.sort()

print("REMOVING THE FOLLOWING PLAYER NAMES")
to_remove = []
for player in pld.players:
	if not re.match(r"^[a-zA-Z'\-. ]+$", player):
		print(player.encode())
		to_remove.append(player)

for rem in to_remove:
	pld.players.remove(rem)

formatted_dict = {i: name for i, name in enumerate(pld.players)}

with open("../output/player_lookup_table.json", "w+") as outfile:
	json.dump(formatted_dict, outfile)