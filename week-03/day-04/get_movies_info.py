from flask import Flask
from flask import request
from flask import jsonify,make_response
from movies_info import movie_dict 
from movies_info import movie_list 


app = Flask(__name__)

@app.route('/api')

def api_root():
    movies=[]
    for movie_dict in movie_list:
        movies.append(movie_dict)
    return jsonify(movies)



if __name__ == "__main__":
    app.run()
