
from flask import Flask
from flask import render_template
import random

app = Flask(__name__)



@app.route("/greet")

def greet_John():
    greet_word = ['Hello','Good Morning','Welcome']
    greet_name = ['Angela','Linda','Amy']
    
    return render_template("random_language.html", greet =random.choice(greet_word),name=random.choice(greet_name))

@app.route("/greet2")

def greet_John2():
    greet_word = ['Hello','Good Morning','Welcome']
    greet_name = ['angela','linda','amy']
    
    return render_template("random_language.html", greet =random.choice(greet_word),name=random.choice(greet_name))

@app.route("/products")

def products_display():
    return render_template("products.html",products = [("Milk", 3.59123) , ("Bread", 2.96332) , ("Rice", 0.64111) ])

articles = [
    {
        "content": "Ne istas culpa ha im negat de. Ii perductae evertenda at desuescam. Nudi per ita sui dare ideo sola omne ordo. Sui sex item sane quum. Paucos sicuti tot qui tantae aliquo strata iis tantas. Mo purgantur at affirmans im reddendum co. Pleraque videntur ut ideamque imaginem ha.",
        "seen": ["John", "Jane", "Bob"]
    },
    {
        "content": "Aliud curam seu venti nihil sed istud volui eae qua. Autho ha falsi fidam tangi ut an tactu. Revera per eandem vox coelum videbo nam virtus. Item olim ei se duas ut. Ut mo ut peccato student adorare et diversa. Praecipuis ad conjunctam me percipitur agnoscerem at perfectius respondere. Horum meo porro uno debeo. Fallacem sentiens ha expertus delapsus dubitare ii. Ex ii efficiente et to perspicuae voluptatem arbitrabar.",
        "seen": ["John", "Jane"]
    },
    {
        "content": "Credendi at nequidem exhibere de. Debeo me dicam ex at ferri digna. Coloribus differant disputari vix cogitandi jam stabilire. Perfacile ut reliquiae perfectae ut. Fuisse falsas captum cui volent notior verbis sui. Meam idem nam ope prae isti quia jure hac. Lor durent has secius fronte usu auditu sumpti. Falso nomen aliud vim calor jam alias annos ubi. Movendi sum creatus vim fas majorem attendo propter. Sui videamus uno profecto refutent rom notitiam innumera potuerit.",
        "seen": ["John"]
    },
    {
        "content": "Potui habeo visus ens mea. An vi re continetur me familiarem negationem. Rei inveniri jam viderunt subducam tam imponere jam. Sub cui more ipsi meum.",
        "seen": []
    }
]

@app.route("/articles")

def list_articles():
    return render_template("articles.html", articles=articles)

authors = [
    {
        "id": 100,
        "name": "John",
        "likes": [
            202,
            200
        ]
    },
    {
        "id": 101,
        "name": "jane",
        "likes" : [
            200
        ]
    }
]

posts = [
    {
        "id": 200,
        "author": 100,
        "content": "Difficulty on insensible reasonable in. From as went he they."
    },
    {
        "id": 201,
        "author": 100,
        "content": "Preference themselves me as thoroughly partiality considered on in estimating."
    },
    {
        "id": 202,
        "author": 101,
        "content": "In as name to here them deny wise this. As rapid woody my he me which."
    }
]
# transform posts and authors into transform_posts begin
def transformed_posts(authors,posts):
    transformed_posts = []
    like_by = []
    for post in posts:
        for author in authors:
            transformed_posts_dict = {}
            transformed_posts_dict["id"] = post["id"]
            transformed_posts_dict["author"] = author["name"]
            transformed_posts_dict["content"] = post["content"]

            if post["author"] == author["id"]:
                post["author"] = author["name"]
            
            for like in author["likes"]:
                if like == post["id"]:
                    like_by.append(author["name"])
                transformed_posts_dict["like_by"] = like_by
        transformed_posts.append(transformed_posts_dict)
    return transformed_posts

transformed_posts = transformed_posts(authors,posts)
# transform posts and authors into transform_posts end

@app.route("/posts")
def list_posts():
    return render_template("posts.html", posts=transformed_posts)

@app.route("/")

def base():
    return render_template("base.html")



if __name__ == "__main__":
    app.run()

