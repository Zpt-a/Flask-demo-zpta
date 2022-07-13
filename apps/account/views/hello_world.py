# coding: utf-8
# author: zpta

from flask import url_for

from manage import app


@app.route('/login')
def login():
    # return 'login'
    return '<p>login</p>'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


with app.test_request_context():
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
