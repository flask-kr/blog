from flask import Blueprint, render_template
from gethtml.extractimgs import extract_images
from web.webtoon.model import WEBTOON, WEBTOON_DETAIL

module = Blueprint('webtoon', __name__, template_folder='templates')

@module.route('/webtoon')
def index():
#    imgs = extract_images()

    webtoon = WEBTOON.query.filter(
            WEBTOON.status == 1
        ).order_by(WEBTOON.title_no.desc())
    return render_template('webtoon/index.html', entity=webtoon)

@module.route('/webtoon/sub_list/<id>')
def sub_list(id):
    webtoon = WEBTOON_DETAIL.query.filter(
            WEBTOON_DETAIL.identify_no == id
        ).order_by(WEBTOON_DETAIL.chapter.desc())

    return render_template('webtoon/sub_list.html', entity=webtoon)

@module.route('/webtoon/detail/<detail_id>')
def view(detail_id):
    webtoon = WEBTOON_DETAIL.query.filter(
            WEBTOON_DETAIL.id == detail_id
        )
    return render_template('webtoon/view.html', entity=webtoon)
