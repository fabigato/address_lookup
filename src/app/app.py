""" main script """
from flask import Flask

from .blueprint import blueprint


app = Flask(__name__)
app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=False, processes=4)
