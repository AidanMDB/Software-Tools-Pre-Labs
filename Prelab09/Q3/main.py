import flask
import sqlite3


app = flask.Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return flask.redirect(flask.url_for('create'))


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
    c.execute(f'''INSERT INTO employees (first_name, last_name, id, email)
              VALUES('{first_name}', '{last_name}', {id}, '{email}')''')
    c.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    app.run(port=8050, host='127.0.0.1', debug=True, use_evalex=False)
