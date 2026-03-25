import request
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from python import data_add as da
from python import backend as be
from virt_m import bash_execute as bash_e

vm_html,vm_css = bash_e.bash_interface.admin_vm_front_end()

db = 'PostgresI'
group_name = 'papasitos'

app = Flask(
    __name__,
    template_folder="html_css",
    static_folder="html_css"
)



#pre_added_dir,question_pre_add = da.base_extract('schema.general_file')
user_id = None
role = None

#stores questions info temp
question_pre_add = []
x = False
y = 0
#init load
pre_added_dir = [
        "Table one",
        "Table two",
        "Bar one",
        "Bar two"
    ]






@app.route("/questions_cad", methods=["GET", "POST"])
def questions_cad():
    global x
    print('/questions_cad x:', x)
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
    answer_count=4,x=x
)

@app.route("/save/complete", methods=["GET", "POST"])
def save_complete():
    global x, y
    da.quiz_input(question_pre_add)
    x = False
    y = 0

    return render_template(
        "home.html",
        files=pre_added_dir,
        show_edit=False,
        show_restore=False,
        show_add=False,
        x=x
    )


@app.route("/create_account" , methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
    return render_template("create_account.html")

@app.route("/quiz_prompt_selection", methods=["GET", "POST"])
def quiz_prompt_selection():
    global x, y

    if request.method == "POST":
        y += 1
        x = True

        pt = request.form.get("question_title")
        category = request.form.get("question_category")
        q_style = request.form.get("answer_style")
        a_am = request.form.get("answer_count")
        q_am = request.form.get("blank_count")

        if q_style == "true_false":
            a_am = 2
            q_am = 1

        return render_template(
            "question.html",
            pt=pt,
            category=category,
            q_style=q_style,
            answer_count=int(a_am),
            q_am=int(q_am),
            x=x
        )

    return render_template(
        "quiz_prompt_selection.html",
        pre_added_dir=pre_added_dir,
        x=x
    )

@app.route("/save", methods=["GET", "POST"])
def save():
    global x,user_id,role
    if request.method == "POST":
        pt = request.form.get("pt") #project
        category = request.form.get("category") #ingredient or size
        q_style = request.form.get("q_style") # fill in or t/f
        a_am = request.form.get("a_am") #amount of answers
        q_am = request.form.get("q_am") #amount of questions
        question = request.form.get("question") # question text
        #if not true or false
        a1 = request.form.get("answer_1")
        a2 = request.form.get("answer_2")
        a3 = request.form.get("answer_3")
        a4 = request.form.get("answer_4")
        a5 = request.form.get("answer_5")
        a6 = request.form.get("answer_6")
        #for true and false
        true_false_answer = request.form.get("true_false_answer") # if the choice is either t or f

        if q_style == 'true_false':
            true_false_answer = true_false_answer
        else:
            true_false_answer = False

        group_id = be.group_info()
        group_id = 9999
        group_id = be.group_id()
        user_id = 9999

        #print('project/dir name: ',pt)
        #print('numeric or varchar: ',category)
        #print('t/f or fill in',q_style)
        #print('amount of answer boxes: ',a_am)
        #print('amount of questions: ',q_am)
        #print('if the correct aswer is t or f: ',true_false_answer)
        #print('what the question is', question)
        #print('answera1 : ', a1)
        #print('answera2 : ', a2)
        #print('answera3 : ', a3)
        #print('answera4 : ', a4)
        #print('answera5 : ', a5)
        #print('answera6 : ', a6)

    answer = {
        "user_id":user_id,
        "group_id":group_id,
        "pt": pt,
        "category": category,
        "q_style": q_style,
        "a_am": a_am,
        "q_am": q_am,
        "true_false_answer": true_false_answer,
        "question": question,
        "a1": a1,
        "a2": a2,
        "a3": a3,
        "a4": a4,
        "a5": a5,
        "a6": a6
    }

    question_pre_add.append(answer)
    return render_template("quiz_prompt_selection.html",x=x)

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    global user_id, role
    return render_template("home.html", files=pre_added_dir,show_edit=role,show_restore=role,show_add=role)

@app.route("/admin/vm", methods=["GET"])
def admin_vm():
    if session.get("role") != "admin":
        return redirect("/login")
    res = t.auth()
    if res:
        status = s.bash.status()
        if status:
            vm_data = {
                "vm_name": "quiz-vm",
                "zone": "us-central1-a",
                "status": "RUNNING"
            }
            return render_template(vm_html,css=vm_css, vm=vm_data)
        return render_template(vm_html,css=vm_css)
    else:
        return render_template("admin_vm_er.html",)


@app.route("/login", methods=["GET", "POST"])
def login(fail=False):
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        columns = {"username": email,
        "password": password}
        output = be.validating_user(columns)
        if output['confirmation']:
            session["user_id"] = output['user_id']
            session["role"] = output['role']
            return redirect(url_for("home"))
        else:
            return render_template("login.html",fail_alert=True)
    return render_template("login.html")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    global user_id
    global role
    user_id = None
    role = None
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)