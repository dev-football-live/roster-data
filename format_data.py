import os
import csv
import json

teams = [
"buf", "nwe", "mia", "nyj", "oti", "clt", "htx", "jax", "cin", "pit", "cle", "rav", 
"kan", "rai", "sdg", "den", "dal", "phi", "was", "nyg", "tam", "nor", "atl", "car", 
"gnb", "min", "chi", "det", "ram", "crd", "sfo", "sea"]


class PlayerLookupDict:
	def __init__(self):
		self.lookup_dict = {}
		self.nxt_id = 0

	def add_or_ignore(self, player):
		if player not in self.lookup_dict:
			self.lookup_dict[player] = self.nxt_id
			self.nxt_id += 1



class PlayerTeamDict:
	teammate_dict = {}

def get_yr(team):
	if team == "htx":
		return 2002
	if team == "cle":
		return 1999
	return 1996


pld = PlayerLookupDict()

for team in teams:
	for yr in range(get_yr(team), 2023):
		with open('{}{}.csv'.format(team, yr)) as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			for row in reader:
				pld.add_or_ignore(row[1])


formatted_dict = {value : key for key, value in pld.lookup_dict.items()}

with open("player_lookup_table.json", "w+") as outfile:
    json.dump(formatted_dict, outfile)

