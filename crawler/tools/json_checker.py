import json
path = "./recipe.json"
with open(path, 'r', encoding='utf-8') as f:
    save_data = json.load(f)
url = []
for i in save_data:
    url.append(i["url"])

if len(url) != len(set(url)):
    print("GO")
    for i in range(len(url)):
        for j in range(i+1, len(url)):
            try:
                if save_data[i]['url'] == save_data[j]['url'] and i!=j:
                    save_data = save_data[:j] + save_data[j+1:]
            except:
                pass
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(save_data, f, ensure_ascii=False, indent=2)

else:
    for i in url:
        print(i)
