from flask import Flask, abort

app = Flask(__name__)

@app.route('/', methods=['GET', 'BREW', "POST"])
def teapot():
    abort(418)

@app.errorhandler(418)
def teapot_error_handle(error):
    return "<h1>I'm a teapot (Error 418)</h1>", 418