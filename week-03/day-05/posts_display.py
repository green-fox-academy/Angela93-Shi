from flask import Flask
from flask import render_template

app = Flask(__name__)

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



if __name__ == "__main__":
    app.run()

