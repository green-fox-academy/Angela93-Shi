from flask import Flask
from flask import request
from flask import jsonify,make_response
from movies_info import movie_dict 
from movies_info import movie_list 


app = Flask(__name__)

# [GET] /api/movies
@app.route('/api/movies')

def api_root():
    movies=[]
    for movie_dict in movie_list:
        movies.append(movie_dict)
    return jsonify(movies)

# [GET] /api/movies/<movie_id>
@app.route('/api/movies/<movie_id>')

def get_selected_movie(movie_id):
    movie_id=int(movie_id)
    for movie_dict in movie_list:
        if movie_dict['id'] == movie_id:
            return jsonify(movie_dict)

# [POST] /api/movies
@app.route('/api/movies',methods=['POST'])
def post_movie():
    # key=request.headers['API_KEY']
    if is_right_api():
        try:
            movie_id = request.form['id']
            title = request.form['title']
            year = request.form['year']
            description = request.form['description']
            movies=create_database(movie_id,title,year,description)
            return jsonify(movies),200
        except:
            return "error"
    else:
        error_hint = {"error":"Invalid API_KEY"}
        return jsonify(error_hint),403
    

def is_right_api():
    API_KEY='1234'
    key=request.headers['API_KEY']
    if key == API_KEY:
        return True

def create_database(movie_id,title,year,description):
    create_dict = {}
    create_dict['id'] = movie_id
    create_dict['title'] = title
    create_dict['year'] = year
    create_dict['description'] = description
    
    return create_dict

# [PUT] /api/movies/<movie_id>

@app.route('/api/movies/<movie_id>',methods=['PUT'])
def put_movie(movie_id):
    movie_get_id = request.form['id']
    if movie_id == movie_get_id:
        movie_replaced_id = "2"
        movie_replaced_title = "The Kid Who Would Be King"
        movie_replaced_year = "1990"
        movie_replaced_description = "A band of kids embark on an epic quest to thwart a medieval menace."
        update_dict = update_database(movie_replaced_id,movie_replaced_title,movie_replaced_year,movie_replaced_description)
    
    if is_right_api():
        return jsonify(update_dict),200
    else:
        error_hint = {"error":"No movie found with <movie_id> ID"}
        return jsonify(error_hint),404
 

def update_database(movie_replaced_id,movie_replaced_title,movie_replaced_year,movie_replaced_description):
    update_dict = {}
    update_dict['id'] = movie_replaced_id
    update_dict['title'] = movie_replaced_title
    update_dict['year'] = movie_replaced_year
    update_dict['description'] = movie_replaced_description
    
    return update_dict


# [DELETE] /api/movies/<movie_id>
@app.route('/api/movies/<movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    if is_right_api():
        for movie_dict in movie_list:
            if movie_dict['id'] == int(movie_id):
                del movie_dict['id']
                del movie_dict['title']
                del movie_dict['year']
                del movie_dict['description']

                if movie_dict == {}:
                    movie_list.remove(movie_dict)        
                return jsonify(movie_list)
            else:
                error_hint = {"error":"no movie can be found with <movie_id>"}
                return jsonify(error_hint),404
    else:
        error_hint = {"error":"Invalid API_KEY"}
        return jsonify(error_hint),403


if __name__ == "__main__":
    app.run()
