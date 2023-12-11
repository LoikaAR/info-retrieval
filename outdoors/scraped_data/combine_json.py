import json

files=['./res_myswiss.json', './res_tic_act.json', './res_zer.json', './res_tic_hik.json']

res = list()

for f in files:
    with open(f, 'r') as infile:
        res.extend(json.load(infile))

with open('./res.json', 'w') as output_file:
    json.dump(res, output_file, indent=4, default=str)