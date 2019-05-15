import json
file_path = './posts.json'
with open(file_path, mode='r',encoding='utf-8') as f:
    js = json.load(f)
    print(type(js))
    print(len(js))

# like_count_list=[]
# for i in range(len(js)):
#     a=js[i]
#     like_count_list.append((a["like_count"]))
# print(like_count_list)
sum_list=[]
for i in js:
    if i["comments"] != None:
        coments_list = i["comments"]
        sum=0
        for j in coments_list:
            sum += j["like_count"]
        sum_list.append(sum)
print(sum_list)

most_popular=0
for i in sum_list:
    if i > most_popular:
        most_popular = i
print(most_popular)

for i in js:
  if i["comments"] != None:
        coments_list = i["comments"]
        sum=0
        for j in coments_list:
            sum += j["like_count"]
        if sum == most_popular:
            print(i)




