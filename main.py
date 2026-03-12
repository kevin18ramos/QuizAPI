from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="html_css",
    static_folder="html_css"
)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/questions_cad")
def questions_cad():

    images = [
        "test1.png",
        "test2.png",
        "test3.png",
        "test4.png"
    ]

    return render_template("question.html", images=images)

@app.route("/login")
def login():
    return "Login page coming soon"

@app.route("/logout")
def login():
    return "Login page coming soon"

if __name__ == "__main__":
    app.run(debug=True)