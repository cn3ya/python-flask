from flask import Flask

app = Flask(__name__)

from controller import user, test, index
app.register_blueprint(index.bp)
app.register_blueprint(user.bp)
app.register_blueprint(test.bp)