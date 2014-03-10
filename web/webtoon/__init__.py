from flask import Blueprint, render_template
from gethtml.extractimgs import extract_images
from web.webtoon.model import WEBTOON

module = Blueprint('webtoon', __name__, template_folder='templates')

@module.route('/webtoon')
def index():
#    imgs = extract_images()

    webtoon = WEBTOON.query.filter(
            WEBTOON.status == 1
        ).order_by(WEBTOON.title_no.desc())
    return render_template('webtoon/index.html', entity=webtoon)

