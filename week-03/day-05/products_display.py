from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/products")

def products_display():
    return render_template("products.html",products = [("Milk", 3.59123) , ("Bread", 2.96332) , ("Rice", 0.64111) ])

if __name__ == "__main__":
    app.run()

