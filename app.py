#!/usr/bin/env python
from flask import Flask, render_template
import datetime

app = Flask(__name__)

app.debug = False


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


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/publications')
def pubs():
    return render_template('pubs.html')


@app.context_processor
def inject_now():
    return {'now': datetime.datetime.utcnow()}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
