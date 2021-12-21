from logging import debug
from flask import Flask, render_template, request, jsonify
from flask.wrappers import Request
from werkzeug.utils import redirect
from torch_utils import transform_image, get_prediction
# from werkzeug import redirect

app = Flask(__name__)


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    # xxx.png
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({'error': 'no file'})
        if not allowed_file(file.filename):
            return jsonify({'error': 'format not supported'})

        try:
            img_bytes = file.read()
            tensor = transform_image(img_bytes)
            prediction = get_prediction(tensor)
            data = {'prediction': prediction.item(), 'class_name': str(prediction.item())}
            return jsonify(data)
        except:
            return jsonify({'error': 'error during prediction'})

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/loading")
def generate_loading():
    return render_template('loading.html')

@app.route("/minting")
def minting():
    return render_template('minting.html')

@app.route("/post", methods=["POST"])
def post_hub():
    # all page redirect works via this function
    if request.form.get('start-service'):
        return redirect('/input')
    if request.form.get('gen-pic'):
        return redirect('/loading')


@app.route("/input")
def input_data():
    return render_template('input.html')

#def minting():
#    pass

@app.route("/result")
def generate_img():
    return render_template('result.html')

def generate_nft():
    pass

if __name__ == '__main__':
    app.run(port=5000, debug=True)