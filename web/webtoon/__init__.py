from flask import Blueprint, render_template
from gethtml.extractimgs import extract_images
from web.webtoon.model import WEBTOON, WEBTOON_DETAIL
from sqlalchemy import distinct

module = Blueprint('webtoon', __name__, template_folder='templates')

@module.route('/webtoon')
def index():
#    imgs = extract_images()

    webtoon = WEBTOON.query.filter(
            WEBTOON.status == 1
        )
    return render_template('webtoon/index.html', entity=webtoon)

@module.route('/webtoon/sub_list/<id>')
def sub_list(id):
    webtoon = WEBTOON_DETAIL.query.filter(
            WEBTOON_DETAIL.identify_no == id,
        ).order_by(WEBTOON_DETAIL.id.desc()).group_by(WEBTOON_DETAIL.chapter)

    return render_template('webtoon/sub_list.html', entity=webtoon)

@module.route('/webtoon/<id>/detail/<detail_id>')
def view(id,detail_id):
    webtoon = WEBTOON_DETAIL.query.filter(
            WEBTOON_DETAIL.identify_no == id,
            WEBTOON_DETAIL.chapter == detail_id
        ).order_by(WEBTOON_DETAIL.id.asc())
    return render_template('webtoon/view.html', entity=webtoon)
