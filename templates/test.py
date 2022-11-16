import json

json_open = open('recipe.json', mode = 'r', encoding = 'UTF-8')
json_load = json.load(json_open)

"""
1. 材料を格納するリストを作る
2. json_loadをfor文に入れる
3. extendを使ってi["tags"]を材料を格納するリストに入れる
4. set()関数で重複を消せる

"""
ing_list = []
for i in json_load:
  ing_list.extend(i["tags"])

ing_list = list(set(ing_list))

print(ing_list)