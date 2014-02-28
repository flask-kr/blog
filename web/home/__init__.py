from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

home = Blueprint('home', __name__, template_folder='templates')

@home.route('/home')
def index():
    try:
        print "here11"
        return render_template('home/index.html')
    except TemplateNotFound:
        abort(404)
