from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'GMsolutions'

    socketio.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app