from flask.ext.script import Manager
from app import create_app

app = create_app("dev")
manager = Manager(app)

@app.route("/")
def index():
    return "Hi there"

if __name__ == "__main__":
    manager.run()
