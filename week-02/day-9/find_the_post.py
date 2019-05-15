import json
file_path = './posts.json'
with open(file_path, mode='r',encoding='utf-8') as f:
    js = json.load(f)
    print(type(js))
    print(len(js))

like_count_list=[]
for i in range(len(js)):
    a=js[i]
    like_count_list.append((a["like_count"]))
print(like_count_list)

most_like=max(like_count_list)
print(most_like)

for i in range(len(js)):
    a=js[i]
    if most_like == a["like_count"]:
        print(js[i])