from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)


    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/page/<page_name>')
    def page(page_name):
        return render_template(f'{page_name}.html')   
    return app
