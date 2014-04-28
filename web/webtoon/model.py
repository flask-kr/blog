from web import create_db
#from sqlalchemy.orm import cloumn_property

from sqlalchemy.sql import and_
from sqlalchemy.ext.hybrid import hybrid_property

db = create_db()

class WEBTOON(db.Model):

    __tablename__ = 'TB_WEBTOON'
    title = db.Column('TITLE', db.String(255), primary_key=True)
    title_no = db.Column('TITLE_NO', db.String(20))
    site_name = db.Column('SITE_NAME', db.String(10))
    image_url = db.Column('IMAGE_URL', db.String(255))
    status = db.Column('STATUS', db.Integer)

class WEBTOON_DETAIL(db.Model):

    __tablename__ = 'TB_WEBTOON_DETAIL'
    id = db.Column('ID', db.String(255), primary_key=True)
    identify_no = db.Column('IDENTIFY_NO', db.String(255))
    chapter = db.Column('CHAPTER', db.String(255))
    list_title_url = db.Column('LIST_TITLE_URL', db.String(255))
    detail_url = db.Column('DETAIL_URL', db.String(255))
