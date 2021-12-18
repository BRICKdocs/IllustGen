from logging import debug
from flask import Flask, render_template, request
from flask.wrappers import Request
from werkzeug.utils import redirect
# from werkzeug import redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/loading")
def generate_loading():
    pass

@app.route("/post", methods=["POST"])
def post_hub():
    # all page redirect works via this function
    if request.form.get('start-service'):
        return redirect('/input')


@app.route("/input")
def input_data():
    return render_template('input.html')

def minting():
    pass

@app.route("/result")
def generate_img():
    pass

def generate_nft():
    pass

if __name__ == '__main__':
    app.run(port=5000, debug=True)