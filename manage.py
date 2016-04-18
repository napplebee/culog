#!/usr/bin/env python
from flask.ext.script import Manager
from app import create_app

app = create_app("culog")

@app.errorhandler(404)
def page_not_found(e):
    return "404"
    # return render_template('front/404.html'), 404

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
