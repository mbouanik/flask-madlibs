from flask import Flask, render_template, request
from stories import story, Story
from re import findall

app = Flask(__name__)

all_stories = [
    "Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}.",
    "I love to {verb} {plural_noun}.",
    "Welcomt to the {place} where you can {verb} or also enjoy {adjective} {noun}",
]


@app.route("/", methods=["GET", "POST"])
def home():
    # mad_lib = None
    # if request.args:
    #     questions = [
    #         question[1:-1]
    #         for question in findall("{[a-zA-Z_]+}", request.args["mad_lib"])
    #     ]
    #     mad_lib = request.args["mad_lib"]
    # else:
    #     questions = story.prompts
    return render_template("index.html", all_stories=all_stories)


@app.route("/form", methods=["GET", "POST"])
def form():
    # mad_lib = None
    # questions = []
    print(list(request.args)[0])
    if request.args.get("mad_lib"):
        questions = [
            question[1:-1]
            for question in findall("{[a-zA-Z_]+}", request.args["mad_lib"])
        ]
        mad_lib = request.args["mad_lib"]
    else:
        questions = [
            question[1:-1]
            for question in findall("{[a-zA-Z_]+}", list(request.args)[0])
        ]
        mad_lib = list(request.args)[0]
    return render_template("form.html", questions=questions, mad_lib=mad_lib)


@app.route("/story")
def strory():
    if request.args.get("mad_lib"):
        new_story = Story(list(request.args["questions"]), request.args["mad_lib"])
        mad_story = new_story.generate(request.args)
    else:
        mad_story = story.generate(request.args)
    return render_template("story.html", story=mad_story)


if __name__ == "__main__":
    app.run(debug=True)
