import json
with open('config.json','r') as f:
	op = json.load(f)
print(op['token'])