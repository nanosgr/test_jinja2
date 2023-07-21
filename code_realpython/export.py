# export.py
from jinja2 import Environment, FileSystemLoader

MAX_SCORE = 100

students = [
    {"name":"Willow", "score":100},
    {"name":"Cordelia", "score":85},
    {"name":"Oz", "score":95},
    {"name":"Buffy", "score":65},
    {"name":"Xander", "score":45},
]

env = Environment(loader=FileSystemLoader("templates/"))
template = env.get_template("export.csv")

filename = f"output/py_challenge.csv"
context = {
    "students":students,
    "max_score":MAX_SCORE,
}

with open(filename, mode="w", encoding="utf-8") as output:
    output.write(template.render(context))
