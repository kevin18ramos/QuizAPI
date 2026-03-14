from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="html_css",
    static_folder="html_css"
)

@app.route("/")
def home():
    files = [
            "file name",
            "file name",
            "file name",
            "file name"
        ]
    return render_template("home.html", files=files)


@app.route("/questions_cad")
def questions_cad():

    return render_template(
    "question.html",
    answer_count=3
)

@app.route("/login")
def login():
    return "Login page coming soon"

@app.route("/logout")
def logout():
    return "Login page coming soon"

if __name__ == "__main__":
    app.run(debug=True)