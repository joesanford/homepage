#!/usr/bin/env python
from flask import Flask, render_template

app = Flask(__name__)

app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects_homeauto')
def homeauto():
    return render_template('homeauto.html')

@app.route('/projects_guitarpp')
def guitarpp():
    return render_template('guitarpp.html')

@app.route('/projects_blockytalky')
def blockytalky():
    return render_template('blockytalky.html')

@app.route('/projects_other')
def projects():
    return render_template('projects.html')

@app.route('/publications')
def pubs():
    return render_template('pubs.html')

if __name__ == '__main__':
    app.run()