import json
path1 = './recipe.json'
path2 = './backup.json'

with open(path1, 'r', encoding='utf-8') as f:
    data1 = json.load(f)
with open(path2, 'r', encoding='utf-8') as f:
    data2 = json.load(f)

print(f"origin: {len(data2)}")
print(f"new: {len(data1)}")