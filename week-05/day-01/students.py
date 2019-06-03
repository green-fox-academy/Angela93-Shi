from collections import Counter

# Given a list of students with the following fields: name, age, gender and grades
students=[
    {'name':'John','age':16,'gender':'male','grades':[5,5,4,2]},
    {'name':'Jane','age':15,'gender':'female','grades':[4,3,4,4,5]},
    {'name':'Bob','age':17,'gender':'male','grades':[2,2,3,1]}
]

# 01 Create a new list that only includes the boys
result_list1 = list(filter(lambda x:x['gender'] == 'male',students))
# print(result_list1)

# 02 Create a new list that only includes who's name starts with the letter J
result_list2 = list(filter(lambda x:x['name'].startswith('J'),students))
# print(result_list2)

# 03 Create a new list that only includes the girls
result_list3 = list(filter(lambda x:x['gender'] == 'female',students))
# print(result_list3)

# 04 Create a new list that only includes who's grade average is above 4
result_list4 = list(filter(lambda x:(sum(x['grades']) / float(len(x['grades']))) >= 4.0 , students))
# print(result_list4)

# 05 Create a new list that only includes the boys who's name starts with the letter J
result_list5= list(filter(lambda x:x['name'].startswith('J') and x['gender'] == 'male' ,students))
# print(result_list5)

# 06 Create a new list that only includes the girls who's grade average is above 4
result_list6 = list(filter(lambda x:(sum(x['grades']) / float(len(x['grades']))) >= 4.0 and x['gender'] == 'female', students))
# print(result_list6)

# 07 Create a new list that only includes who's at least two 5s
result_list7 = list(filter(lambda x:x['grades'].count(5) == 2,students))
# print(result_list7)

# 08 SCreate a new list that only includes who's grade average is above 4 and at at least got two 5s
result_list8 = list(filter(lambda x:(sum(x['grades']) / float(len(x['grades']))) >= 4.0 and x['grades'].count(5) == 2,students))
# print(result_list8)