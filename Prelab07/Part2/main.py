import flask
import sqlite3
import hashlib
from datetime import datetime


def hash_func(get_hashed):
    hashed_id = hashlib.sha256(get_hashed.encode('utf-8')).hexdigest()
    return hashed_id

def insert_user(hashed_id, first_name, last_name, email):
    conn = sqlite3.connect("Part2/data/users.db")
    c = conn.cursor()
    c.execute(f"INSERT INTO user_info (user_id, first_name, last_name, email) VALUES('{hashed_id}', '{first_name}', '{last_name}', '{email}')")
    c.close()
    conn.commit()
    conn.close()

def find_user(hashed_id):
    try:
        conn = sqlite3.connect("Part2/data/users.db")
        c = conn.cursor()
        c.execute("SELECT EXISTS (SELECT 1 from user_info where user_id=?)", (hashed_id, ))
        c.close()
        conn.close()
        print("yes")
        return True
    except:
        return False

def get_user(hashed_id):
    conn = sqlite3.connect("Part2/data/users.db")
    c = conn.cursor()
    user = None
    user = c.execute(f"SELECT first_name,last_name,email FROM user_info WHERE user_id=?", (hashed_id, )).fetchone()
    c.close()
    conn.close()
    return user

def get_user_posts(hash_id):
    conn = sqlite3.connect("Part2/data/users.db")
    c = conn.cursor()
    user = None
    user = c.execute(f"SELECT * FROM user_posts WHERE user_id=?", (hash_id, )).fetchall()
    c.close()
    conn.close()
    return user

def insert_post(hash_id, post_id, post_title, post_content, post_date):
    conn = sqlite3.connect("Part2/data/users.db")
    c = conn.cursor()
    c.execute(f"INSERT INTO user_posts (user_id, post_id, title, content, date) VALUES('{hash_id}', '{post_id}', '{post_title}', '{post_content}', '{post_date}')")
    c.close()
    conn.commit()
    conn.close()

def get_post(post_id):
    conn = sqlite3.connect("Part2/data/users.db")
    c = conn.cursor()
    post = None
    post = c.execute(f"SELECT * FROM user_posts WHERE post_id=?", (post_id, )).fetchone()
    c.close()
    conn.close()
    return post


app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def route():
    return flask.redirect('/register')

@app.route('/register', methods=['GET'])
def register():
    return flask.render_template('register.html')

@app.route('/register', methods=['POST'])
def submit_register():
    user_name = flask.request.form['uname']
    pass_word = flask.request.form['pword']

    id = user_name + pass_word
    id = hash_func(id)

    if find_user(id):       # if user exists
        return flask.redirect(f'/{id}/profile')
    else:
        return flask.redirect(f'/signup/{id}')



@app.route('/signup/<ucode>', methods=['GET'])
def signup(ucode):
    return flask.render_template('signup.html')

@app.route('/signup/<ucode>', methods=['POST'])
def signup_submit(ucode):
    first_name_sub = flask.request.form['fname']
    last_name_sub = flask.request.form['lname']
    email_sub = flask.request.form['mail']

    insert_user(ucode, first_name_sub, last_name_sub, email_sub)

    return flask.redirect(f'/{ucode}/profile')



@app.route('/<ucode>/profile', methods=['GET'])
def profile(ucode):
    user_prof = get_user(ucode)
    user_posts = get_user_posts(ucode)
    return flask.render_template('profile.html', data=user_prof, posts=user_posts, id=ucode)



@app.route('/<ucode>/create', methods=['GET'])
def create_post(ucode):
    return flask.render_template('create.html')

@app.route('/<ucode>/create', methods=['POST'])
def create_post_sub(ucode):
    title = flask.request.form['ptitle']
    contents = flask.request.form['pcontent']
    date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    post_id = ucode + date
    post_id = hash_func(post_id)

    insert_post(ucode, post_id, title, contents, date)

    return flask.redirect(f'/{ucode}/profile')


@app.route('/posts/<postcode>', methods=['GET'])
def view_post(postcode):
    full_post = get_post(postcode)
    return flask.render_template('post_page.html', post=full_post)


if __name__ == '__main__':
    app.run(port=8051, host='127.0.0.1', debug=True, use_evalex=False)