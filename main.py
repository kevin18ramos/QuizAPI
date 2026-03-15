from flask import Flask, render_template, request, jsonify
from python import data_add as da

app = Flask(
    __name__,
    template_folder="html_css",
    static_folder="html_css"
)

@app.route("/")
def home():
    files = [
        "Table one",
        "Table two",
        "Bar one",
        "Bar two"
    ]
    return render_template("home.html", files=files,
        show_edit=False,
        show_restore=False,
        show_add=False)


@app.route("/questions_cad", methods=["GET", "POST"])
def questions_cad():
    if request.method == "POST":
        q = request.form.get("q")
        answ_one = request.form.get("answ_one")
        answ_two = request.form.get("answ_two")
        answ_three = request.form.get("answ_three")
        answ_four = request.form.get("answ_four")

        result = da.create_quiz(
            answ_one,
            answ_two,
            answ_three,
            answ_four
        )

        return jsonify(result)

    return render_template(
    "question.html",
    answer_count=4
)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/create_account" , methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
    return render_template("create_account.html")

@app.route("/quiz_prompt_selection", methods=["GET", "POST"])
def quiz_prompt_selection():
    if request.method == "POST":
        pt = request.form.get("question_title")
        category = request.form.get("question_category")
        q_style = request.form.get("answer_style")
        a_am = request.form.get("answer_count")
        q_am = request.form.get("blank_count")

        #category: ingredient
        #q_style: true_false
        #category: amount
        #q_style: fill_blank

        if q_style == 'true_false':
            a_am = 2
            q_am = 0

        return render_template(
            "question.html",
            pt=pt,
            category=category,
            q_style=q_style,
            answer_count=int(a_am),
            q_am=int(q_am) #will need to be coded
        )

        return jsonify(result)
    return render_template("quiz_prompt_selection.html")

def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    return "Login page coming soon"

if __name__ == "__main__":
    app.run(debug=True)