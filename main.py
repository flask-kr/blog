from web import create_app
#from web import home
from web.home import home
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

if __name__ == '__main__':
    app.run("0.0.0.0", debug=app.config['DEBUG'])
