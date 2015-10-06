from flask import render_template

from . import front as front_bp

@front_bp.route("/")
def index():
    return render_template('index.html')
