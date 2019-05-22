from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/movies_index')
def my_movies():
    return render_template('movies_index.html')

@app.route('/movies_index/<username>')
def go_to_movie1(username):
    return render_template(f'{username}')


if __name__ == "__main__":
    app.run()