# From http://blog.thedataincubator.com/2015/09/painlessly-deploying-data-apps-with-bokeh-flask-and-heroku/
from flask import Flask,render_template
app_lulu = Flask(__name__)

@app_lulu.route('/index_lulu')
def index_lulu():
    return(render_template('userinfo_lulu.html'))

if __name__ == '__main__':
    app_lulu.run(debug=True)
