import json
import wanakana

json_open = open('fixture/recipe2.json', mode = 'r', encoding = 'UTF-8')
json_data = json.load(json_open)
json_open.close()
with open("ing_rule.txt", encoding="utf-8", mode="r") as f:
    texts = f.readlines()
texts.sort(key=len)
texts.reverse()
for item in range(len(json_data)):
    for ing in range(len(json_data[item]["tags"])):
        for text in texts:
            if wanakana.to_hiragana(text.replace("\n", "")) in wanakana.to_hiragana(json_data[item]["tags"][ing]):
                json_data[item]["tags"][ing] = text.replace("\n", "").split("(")[0]
                json_data[item]["tags"][ing] = json_data[item]["tags"][ing].split("（")[0]
    json_data[item]["tags"] = list(set(json_data[item]["tags"]))

with open("fixture/recipe2_fix.json", mode="w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)