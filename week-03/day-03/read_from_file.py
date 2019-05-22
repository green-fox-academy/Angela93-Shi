from flask import Flask
from flask import render_template
import re

def read_txt():
    f=open("movies_id.txt")
    datas=f.readlines()
    for data in datas:
        data=f.readlines()
    f.close()
    return datas

p=re.compile(r'(\".+\")\s(\".+\"$)')

def get_dic(list_num):
    movie_dic = {}
    for i in list_num:
        movie_name = (p.match(i)).group(1)
        movie_description = (p.match(i)).group(2)
        movie_dic[movie_name] = movie_description
    return movie_dic

def get_title_description(dict):
    for key,values in dict.items():
        return key
        
app = Flask(__name__)
@app.route('/the_movie/<title>')

def mapping_movie(title):
    return render_template('the_movie.html',movietitle = title,description = dict[title])


list_num = read_txt()
dict = get_dic(list_num)
title= get_title_description(dict)

if __name__ == "__main__":
    app.run()


# test url : http://127.0.0.1:5000/the_movie/"Glass"