import flask
import sqlite3


app = flask.Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return flask.redirect(flask.url_for('home'))

@app.route("/home", methods=['GET'])
def home():
    return flask.render_template("home.html")

@app.route("/create", methods=['GET'])
def form():
    return flask.render_template("form.html")

@app.route("/create", methods=['POST'])
def submit_form():
    first_name_sub = flask.request.form['fname']
    last_name_sub = flask.request.form['lname']
    id_sub = flask.request.form['idlabel']
    email_sub = flask.request.form['mail']

    insert_employee_data(first_name_sub, last_name_sub, id_sub, email_sub)

    return flask.render_template("form.html")

def insert_employee_data(first_name, last_name, id, email):
    conn = sqlite3.connect("data/company.db")
    c = conn.cursor()
    c.execute(f"INSERT INTO employees (first_name, last_name, id, email) VALUES('{first_name}', '{last_name}', {id}, '{email}')")
    c.close()
    conn.commit()
    conn.close()



""" 
@app.route("/view", methods=['GET', 'POST'])
def view():
    ecode = flask.request.args.get('emp_id')    
    return flask.redirect(f"/view/{ecode}")
 """


@app.route("/view/<ecode>", methods=['GET', 'POST'])
def view_dynamic_employee(ecode):
    id = ecode
    employee = fetch_employee(id)
    return flask.render_template("view_id.html", data=employee)

def fetch_employee(ecode):
    conn = sqlite3.connect("data/company.db")
    c = conn.cursor()
    employee = None
    employee = c.execute(f"SELECT first_name,last_name,email from employees where id={ecode}").fetchone()

    if employee is None:
        raise ValueError(f"employee {ecode} does not exist")
    
    c.close()
    conn.close()
    return employee

def delete_employee(ecode):
    conn = sqlite3.connect("data/company.db")
    c = conn.cursor()
    c.execute(f"DELETE FROM employees WHERE id={ecode}")
    c.close()
    conn.commit()
    conn.close()


@app.route("/view_all", methods=['GET'])
def view_all():
    conn = sqlite3.connect("data/company.db")
    c = conn.execute("SELECT * from employees").fetchall()

    employee_list = []
    for employee in c:
        employee_list.append((employee[0], employee[1], employee[3]))

    return flask.render_template("view_all.html", data = employee_list)



if __name__ == '__main__':
    app.run(port=8050, host='127.0.0.1', debug=True, use_evalex=False)