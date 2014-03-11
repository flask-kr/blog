from flask import Blueprint, render_template
from web.board.model import BOARD

module = Blueprint('board', __name__, template_folder='templates')

@module.route('/board')
def index():
    return render_template('board/index.html')
