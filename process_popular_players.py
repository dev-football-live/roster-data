import json
with open('pop_player.txt') as f:
    output = f.readlines()

output = [p.replace("\n", "") for p in output]

with open('player_lookup_table.json') as data_file:
    data = json.load(data_file)

names = [v for k, v in data.items()]

not_in = [p for p in output if p not in names]

print(not_in)