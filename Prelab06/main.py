import flask
import sqlite3


app = flask.Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return flask.redirect(flask.url_for('home'))

@app.route("/home", methods=['GET'])
def home():
    return flask.render_template("home.html")

@app.route("/form", methods=['GET'])
def form():
    return flask.render_template("form.html")

@app.route("/form", methods=['POST'])
def submit_form():
    first_name_sub = flask.request.form['fname']
    last_name_sub = flask.request.form['lname']
    id_sub = flask.request.form['idlabel']
    email_sub = flask.request.form['mail']

    
    # sqlite3.connect("/data/company.db")
    return flask.render_template("form.html")

@app.route("/view_all", methods=['GET'])
def view_all():
    conn = sqlite3.connect("/data/company.db")
    c = conn.execute("SELECT * from employees").fetchall()

    employee_list = []
    for employee in c:
        employee_list.append({employee[0], employee[1], employee[3]})

    return flask.render_template("view_all.html", data = employee_list)


def fetch_employee(ecode):
    conn = sqlite3.connect("/data/company.db")
    c = conn.cursor()
    employee = None
    employee = c.execute("SELECT first_name,last_name,email from employees where id = ?", (ecode)).fetchone()

    if employee is None:
        raise ValueError(f"employee {ecode} does not exist")
    

    c.close()
    conn.close()
    return employee

if __name__ == '__main__':
    app.run(port=8050, host='127.0.0.1', debug=True, use_evalex=False)