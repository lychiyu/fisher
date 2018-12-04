from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    # 将蓝图注册到flask核心对象app上
    from app.web.book import web
    app.register_blueprint(web)
