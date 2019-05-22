from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

products = [
    {'id':1,'name':'display','price':'100','qty':'5'},
    {'id':2,'name':'SSD-256GB','price':'70','qty':'10'},
    {'id':3,'name':'HDD-1TB','price':'50','qty':'10'},
    {'id':4,'name':'RAM-8GB','price':'50','qty':'3'},
    {'id':5,'name':'RAM-16GB','price':'150','qty':'1'},
    {'id':6,'name':'keyboard','price':'15','qty':'0'},
    {'id':7,'name':'cooler','price':'40','qty':'4'}
]

@app.route('/')
def products_search():
    return render_template('product_search.html')


@app.route("/result", methods=['GET','POST'])
def products_search_result():
    if request.method == 'GET':
        name = request.args.get("product_name")
        price = request.args.get("product_price")
        qty = request.args.get("product_qty")
        result = search_the_result(name, price, qty)
        return render_template("products_search_result.html", result=result)

    elif request.method == 'POST':
        pass

def search_the_result(name, price, qty):
    result = []
    for i in range(len(products)):
        product = products[i]

        if product["name"] == name:
            result.append(product)

        if product["price"] == price:
            result.append(product)
            
        if product["qty"] == qty:
            result.append(product)

    return result


if __name__ == "__main__":
    app.run()