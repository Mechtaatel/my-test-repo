import json
t = {100: '1', 100: '10'}
with open('test.json','w') as f:
	json.dump(t, f)
with open('test.json','r') as f:
	op = json.load(f)
print(op)