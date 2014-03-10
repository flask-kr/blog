from web import create_db
#from sqlalchemy.orm import cloumn_property

from sqlalchemy.sql import and_
from sqlalchemy.ext.hybrid import hybrid_property

db = create_db()

class WEBTOON(db.Model):

    __tablename__ = 'TB_FAVORITE_WEBTOON'
    title = db.Column('TITLE', db.String(255), primary_key=True)
    title_no = db.Column('TITLE_NO', db.String(20))
    image_url = db.Column('IMAGE_URL', db.String(255))
    status = db.Column('STATUS', db.Integer)
