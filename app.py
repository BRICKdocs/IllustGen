from flask import Flask, render_template, request
from werkzeug.utils import redirect
# from keras.models import load_model
# from keras.preprocessing import image

# from torch_utils import transform_image, get_prediction
# from werkzeug import import_string, cached_property
# from app import LazyView

app = Flask(__name__)


# dic = {0 : 'Cat', 1 : 'Dog'}

# model = load_model('model.h5')

# model.make_predict_function()

# def predict_label(img_path):
# 	i = image.load_img(img_path, target_size=(100,100))
# 	i = image.img_to_array(i)/255.0
# 	i = i.reshape(1, 100,100,3)
# 	p = model.predict_classes(i)
# 	return dic[p[0]]


# initialize IMAGE DATA TYPE
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    # xxx.png
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Start the index
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/post", methods=["POST"])
def post_hub():
    # all page redirect works via this function
    if request.form.get('start-service'):
        return redirect('/input')
    if request.form.get('gen-pic'):
        return redirect('/result')

@app.route("/input")
def input_data():
    return render_template('input.html')


@app.route("/result")
def generate_img():
    return render_template('result.html')





if __name__ == '__main__':
    app.run(port=5000, debug=True)