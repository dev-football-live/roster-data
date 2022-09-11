import os
import csv
import json

data = json.load(open('player_lookup_table.json'))

number_name_dict = {int(k) : v for k, v in data.items()}
name_number_dict = {v: int(k) for k, v in data.items()}
#print(name_number_dict)

new_players = [v for k, v in number_name_dict.items()]
new_players.sort()

new_dict = {k: v for k, v in enumerate(new_players)}
print(new_dict)

with open("player_lookup_table_alphabetized.json", "w+") as outfile:
    json.dump(new_dict, outfile)