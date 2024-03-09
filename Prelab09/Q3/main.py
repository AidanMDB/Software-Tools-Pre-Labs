import flask
import sqlite3


app = flask.Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return flask.render_template("form.html")


@app.route("/", methods=['POST'])
def submit_form():
    id_sub = flask.request.form['idlabel']

    emp_data = retrieve_employee_data(id_sub)
    return flask.render_template("display.html", employee=emp_data)


def retrieve_employee_data(id):
    conn = sqlite3.connect("Q3/database.db")
    c = conn.cursor()
    print(f'SELECT id,first_name,last_name,email FROM employees WHERE id={id}')
    employee = c.execute(f'''SELECT id,first_name,last_name,email FROM
                         employees WHERE id={id}''').fetchone()
    c.close()
    conn.commit()
    conn.close()
    return employee


if __name__ == '__main__':
    app.run(port=8050, host='127.0.0.1', debug=True, use_evalex=False)
    print("---------FIRST command that causes an SQL injection----------\n")
    print("1 OR 1=1") # noqa
    print("\n The URL for this command is given below : \n")
    print("http://127.0.0.1:8050/") # noqa

    print("---------SECOND command that causes an SQL injection----------\n")
    print("id = 1234 UNION SELECT username, password FROM users;") # noqa
    print("\n The URL for this command is given below : \n")
    print("http://127.0.0.1:8050/") # noqa

    print("---------THIRD command that causes an SQL injection----------\n")
    print("12345 or first_name = 'aidan'") # noqa
    print("\n The URL for this command is given below : \n")
    print("http://127.0.0.1:8050/") # noqa

    print("---------FOURTH command that causes an SQL injection----------\n")
    print("1 UNION ALL SELECT id, password, null, null FROM passwords--") # noqa
    print("\n The URL for this command is given below : \n")
    print("http://127.0.0.1:8050/") # noqa
