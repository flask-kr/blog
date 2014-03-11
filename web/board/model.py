from web import create_db

from sqlalchemy.sql import and_

db = create_db()

class BOARD(db.Model):

    __tablename__ = 'TB_BOARD'
    id = db.Column('ID', db.Integer, primary_key=True)
    title = db.Column('TITLE', db.String(70))
    writer = db.Column('WRITER', db.String(20))
    comment = db.Column('COMMENT', db.String(255))
    created_at = db.Column('CREATED_AT', db.String(45))