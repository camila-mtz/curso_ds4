from flask import Flask

app = Flask(__name__)

@app.route("/") # Home or root of website
def index():
    '''Funcion que se ejecuta cuando se accede a la raiz de la pagina'''
    return '''<html>
                <head>
                    <title>HELLO WORLD</title>
                </head>
                <body><h1>Hello world</h1>
                    <p>Ir a la pagina de <a href="/about">Acerca de</a></p>
                </body>
            </html>'''

@app.route("/about") # Info about this site
def about():
    '''Funcion que se ejecuta cuando se accede a la pagina de Acerca de'''
    return '''<html>
                <head>
                    <title>Acerca de</title>
                </head>
                <body><h1>Acerca de</h1>
                    Ir a la pagina de <a href="/">Inicio</a></p>
                </body>
            </html>'''

if __name__ == "__main__":
    app.run(debug=True)