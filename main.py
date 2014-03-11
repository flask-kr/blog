from web import create_app, create_db
#from web import home
from web.home import module as home
from web.webtoon import module as webtoon
from web.board import module as board
from flask import Flask
from flask import render_template_string

app = create_app()
app.config.from_pyfile('../config.py')

@app.route('/')
def index():
    return render_template_string('<h1>Hello World</h>')

# register blueprints
#app.register_blueprint(home, url_prefix='/home')
app.register_blueprint(home)
app.register_blueprint(webtoon)
app.register_blueprint(board)

# init db
db = create_db()
db.init_app(app)
#db.app = app
#db.create_all()

if __name__ == '__main__':
    app.run("0.0.0.0",port=4000, debug=app.config['DEBUG'])
