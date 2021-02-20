#!/usr/bin/env python
from flask.ext.script import Manager
from app import create_app

app = create_app("culog")
# for debug:
app.debug = True
manager = Manager(app)

if __name__ == "__main__":
    # app.run(None, None, True)
    manager.run()
