from flask import Flask, session
from flask import request
from flask import abort,redirect, url_for
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
  return 'Hello world'

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    session['username'] = request.form['username']
    return redirect(url_for('index'))
  return render_template('login.html')

@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('index'))

app.secret_key = '\x16Y\xe7\x97\x0e\x84n\ntH\xa3\x107I3kE\xa0\xc8\xaayFYz'

