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
        sources = []
        with open('sources.txt', 'r') as f:
            for line in f:
                sources.append(line.strip())
        return render_template('sources.html', sources=sources)
    
    @app.route("/wahlomat", methods=["POST"])
    def wahlomat():
        A1 = request.form.get("1")
        A2 = request.form.get("2")
        A3 = request.form.get("3")
        A4 = request.form.get("4")
        A5 = request.form.get("5")
        result = sum([int(A1), int(A2), int(A3), int(A4), int(A5)])
        if result > 1:
            answer = "Marktorientiert"
        
        elif result < -1:
            answer = "Moderat Protektionistisch"
        if result > 3:
            answer = "Hyperglobalisierung"
        elif result < -3:
            answer = "Autarkie"
        else:
            answer = "Ausgewogene Herangehensweise"
        result += 5
        result *= 0.1
        return render_template('zollomat_ergebnis.html', answer=answer, result=result)
    return app

app = create_app()
