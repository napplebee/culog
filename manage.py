#!/usr/bin/env python
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from app import create_app

app = create_app("dev")
manager = Manager(app)
bootstrap = Bootstrap(app)

if __name__ == "__main__":
    manager.run()
