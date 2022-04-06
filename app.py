from flask import Flask
from flask import request

from flask import redirect, url_for, abort
from markupsafe import escape


app = Flask(__name__)


@app.route('/welcome/')
@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/Gowreesh/')
def gowreesh():
    return '<h1>Welcome Gowreesh</h1>'


@app.route('/gowreesh/<param>')
def gowreesh_param(param):
    return '<h1>Welcome {}</h1>'.format(escape(param.capitalize()))


@app.route('/add/<int:v1>/<int:v2>/')
def gowreesh_add(v1, v2):
    return '<h1>Answer:{}</h1>'.format(v1+v2)


@app.route('/user/<int:user_id>/')
def gowreesh_user(user_id):
    users = ['G', 'O', 'W']
    try:
        return '<h1>Welcome:{}</h1>'.format(users[user_id])
    except Exception:
        abort(404)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        User = request.form['name']
        return redirect(url_for('gowreesh', param=User))


if __name__ == "__main__":
    app.run(debug=True, port=8080)
