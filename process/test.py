import json

with open('../output/player_lookup_table.json', 'r') as f:
    _json = json.load(f)
    player_lookup_table = {int(k) : _json[k] for k in _json}

with open('../output/player_teammates.json', 'r') as f:
    _json = json.load(f)
    player_teammates = {int(k) : _json[k] for k in _json}


valid_test_cases = [
    ["Aaron Rodgers", "D.J. Reed", "George Kittle"],
    ["Kirk Cousins", "Stefon Diggs", "Josh Allen"],
    ["Calvin Ridley", "Matt Ryan", "Michael Pittman Jr.", "Anthony Richardson"],
    ["Dak Prescott", "Brandin Cooks", "Tom Brady"],
]

invalid_test_cases = [
    ["Aaron Rodgers", "Deebo Samuel", "George Kittle"],
    ["Kirk Cousins", "Fred Warner", "Josh Allen"],
    ["Calvin Ridley", "DeSean Jackson", "Matthew Stafford", "Anthony Richardson"],
    ["Dak Prescott", "Cooper Kupp", "Tom Brady"],
]

inverse_player_lookup = {v : k for k, v in player_lookup_table.items()}
    
for i, test_case in enumerate(valid_test_cases):
    _test_case = test_case[::]

    for name in _test_case:
        assert name in inverse_player_lookup
    
    cur_player = None
    cur_teammates = [k for k in player_teammates]

    try:
        while _test_case:
            cur_player = inverse_player_lookup[_test_case.pop(0)]
            assert cur_player in cur_teammates
            cur_teammates = player_teammates[cur_player]
    except AssertionError as e:
        print(f"Valid test case {i} failed: {valid_test_cases[i]}")
    

for i, test_case in enumerate(invalid_test_cases):
    _test_case = test_case[::]

    for name in _test_case:
        assert name in inverse_player_lookup
    
    cur_player = None
    cur_teammates = [k for k in player_teammates]

    try:
        while _test_case:
            cur_player = inverse_player_lookup[_test_case.pop(0)]
            assert cur_player in cur_teammates
            cur_teammates = player_teammates[cur_player]
        print(f"Invalid test case {i} failed: {invalid_test_cases[i]}")
    except AssertionError as e:
            pass
