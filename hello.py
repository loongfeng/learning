# -*- coding: utf-8 -*-
# @Author: loongfeng
# @Date:   2017-03-17 22:40:57
# @Last Modified by:   loongfeng
# @Last Modified time: 2017-03-18 21:07:05
from flask import Flask, render_template,request
from werkzeug import secure_filename
from flask import make_response
from flask import abort ,redirect,usr_for
app=Flask(__name__)

@app.route('/')
def hello_world():
  username=request.cookies.get('username')
  resp=make_response(render_template())
  resp.set_cookie('username','the username')
  return resp

  return 'hello world'

@app.route('/index/')
def index():
  return 'this is index'

@app.route('/user/<username>')
def show_user_profile(username):
  return 'User %s'%username

@app.route('/post/<int:post_id>')
def show_post(post_id):
  return 'post %d' % post_id
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
  return render_template('hello.html',name=name)

@app.route('/login',methods=['POST','GET'])
def login():
  error=None
  if request.method=='POST':
    if valid_login(request.form['username'],request.form['password']):
      return log_the_user_in(request.form['username'])
    else:
      error ='Invalid username/password'
  return render_template('login.html',error=error)


@app.route('/upload',methods=['GET','POST'])
def upload_file():
  if request.method='POST':
    f=request.files['the file']
    f.save('/var/www/upload/'+secure_filename(f.filename))

if __name__=='__main__':
  app.debug=True
  app.run()
  #app.run(host='0.0.0.0')