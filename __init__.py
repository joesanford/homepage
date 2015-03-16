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

@app.route('/homeauto')
def homeauto():
    return render_template('homeauto.html')

@app.route('/guitarpp')
def guitarpp():
    return render_template('guitarpp.html')

@app.route('/blockytalky')
def blockytalky():
    return render_template('blockytalky.html')

@app.route('/projects')
def projects():
    return render_template('single-project.html')

if __name__ == '__main__':
    app.run()