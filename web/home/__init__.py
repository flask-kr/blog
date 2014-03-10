from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from gethtml.extractimgs import extract_images

module = Blueprint('home', __name__, template_folder='templates')

@module.route('/home')
def index():
    try:
        return render_template('home/index.html')
    except TemplateNotFound:
        abort(404)
