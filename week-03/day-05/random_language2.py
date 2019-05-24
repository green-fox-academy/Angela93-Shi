# Create an application that can greet John in a random language every time the page loads.
# Store the greetings in a list

# <h1>Hello, John!</h1>

from flask import Flask
from flask import request
from flask import render_template
import random

app = Flask(__name__)

@app.route("/greet2")

def greet_John():
    greet_word = ['Hello','Good Morning','Welcome']
    greet_name = ['angela','linda','amy']
    
    return render_template("random_language.html", greet =random.choice(greet_word),name=random.choice(greet_name))



if __name__ == "__main__":
    app.run()

