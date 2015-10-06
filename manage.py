#!/usr/bin/env python
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from app import create_app

from flask import render_template

app = create_app("dev")
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    manager.run()
