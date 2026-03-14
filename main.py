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
        "quiz_1.txt",
        "quiz_2.txt",
        "quiz_3.txt",
        "quiz_4.txt",
        "quiz_5.txt",
        "quiz_6.txt",
        "quiz_7.txt"
    ]
    return render_template("home.html", files=files)


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
    return "Login html"

@app.route("/logout")
def logout():
    return "Login page coming soon"

if __name__ == "__main__":
    app.run(debug=True)