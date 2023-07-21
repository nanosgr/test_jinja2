# app.py
import flask

app = flask.Flask(__name__)

@app.route("/hello/")
def hello():
    return "Hello World!"

@app.route("/")
def home():
    return flask.render_template("base.html", title="Jenny's Server")



MAX_SCORE = 100
TEST_NAME = "Python Challenge"

students = [
    {"name":"Willow", "score":100},
    {"name":"Cordelia", "score":85},
    {"name":"Oz", "score":95},
    {"name":"Buffy", "score":65},
    {"name":"Xander", "score":45},
]

@app.route("/course/")
def course():
    context = {
        "students":students,
        "max_score":MAX_SCORE,
        "test_name":TEST_NAME,
        "title":"Jenny's Server",
    }
    return flask.render_template("course.html", **context)

@app.route("/projects/")
def projects():
    context = {
        "projects":["Computer stuff", "Witchcraft", "Dating Giles"],
        "title":"Jenny's Server",
    }
    return flask.render_template("projects.html", **context)

@app.route("/library/")
def library():
    context = {
        "textbooks":["Science", "Math", "Algebra", "Music", "Art", "History",
            "Gym"],
        "magicbooks":["Grim's Traps", "love spells", "Exorcism" ],
        "statement":'<a href="https://www.imdb.com/name/nm0372117/">Giles</a>',
        "title":"Jenny's Server",
    }
    return flask.render_template("library.html", **context)

@app.route("/tara/")
def tara():
    context = {
        "title":"Jenny's Server",
    }
    return flask.render_template("tara.html", **context)


from dataclasses import dataclass

@dataclass
class Swimmer:
    name: str
    speed: int

@app.route("/swim/")
def swim():
    context = {
        "swimmers":[
            Swimmer("Cameron", 7),
            Swimmer("Dodd", 6),
            Swimmer("Gage", 8),
            Swimmer("Xander", 5),
        ],
        "title":"Jenny's Server",
    }
    return flask.render_template("swim.html", **context)

if __name__ == "__main__":
    app.run(debug=True)
