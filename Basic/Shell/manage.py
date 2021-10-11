from flask_script import Manager
from app import app

# app = Flask(__name__)
# Configure your app

manager = Manager(app)

@manager.command
def hello():
    print("test")

if __name__ == "__main__":
    manager.run()

