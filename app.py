from flask import Flask, render_template, request, send_from_directory


def create_app():
    app = Flask(__name__)


    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/page/<page_name>')
    def page(page_name):
        return render_template(f'{page_name}.html')   

    @app.route('/images/<path:image_name>')
    def images(image_name):
        return send_from_directory('public/images', image_name)

    @app.route('/sources')
    def sources():
        return render_template('sources.html')
    return app

app = create_app()
