from logging import debug
from flask import Flask, render_template
# from werkzeug import redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/loading")
def generate_loading():
    pass

@app.route("/post")
def post_hub():
    # all page redirect works via this function
    pass


@app.route("/input")
def input_data():
    pass

def minting():
    pass

@app.route("/result")
def generate_img():
    pass

def generate_nft():
    pass

if __name__ == '__main__':
    app.run(port=5000, debug=True)