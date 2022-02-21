from re import DEBUG
from flask import blueprints, url_for, render_template, flash, request, session, g
from werkzeug.utils import redirect

bp = blueprints.Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('main.html')

@bp.route('/', methods=["POST"])
def go_draw():
    if request.method =='POST' and request.form['description']:
        description = request.form['description']
        return redirect(url_for('gen.result', description = description))
    else:
        return redirect(url_for('main.index'))

@bp.route('/input', methods=('GET', 'POST'))
def input():
    if request.method =='POST' and request.form['description']:
        description = request.form['description']
        return redirect(url_for('gen.result', description = description))
    return render_template('input.html')