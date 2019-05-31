from flask import Flask
from flask import render_template
from slack_channel import most_messages
from slack_channel import most_emoji
from slack_channel import reacted_most
from slack_channel import most_active

app = Flask(__name__)


@app.route("/messages")
def messages_display():
    result = most_messages()
    result2 = most_active()
    return render_template("message_page.html", messages = result,posts=result2)

@app.route("/reactions")
def reactions_display():
    result = most_emoji()
    result2 = reacted_most()
    return render_template("reaction.html", reactions = result,reactions2=result2)


@app.route("/")

def base():
    return render_template("base.html")



if __name__ == "__main__":
    app.run()