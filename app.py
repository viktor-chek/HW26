import os

from flask import Flask

from db import db
from pages.bp_main.views import main_blueprint
from pages.bp_post_page.views import post_blueprint  # Импорт всех блупринтов
from pages.bp_search.views import search_blueprint
from pages.bp_user_page.views import user_blueprint
from pages.bp_errors.errors import errors_blueprint
from pages.bp_api.views import api_blueprint

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

app = Flask(__name__)  # Создание экземпляра фласк

app.config["JSON_AS_ASCII"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{DB_USER}:{DB_PASSWORD}@postgres/{DB_NAME}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)  # Регистрация блупринтов
app.register_blueprint(user_blueprint)
app.register_blueprint(errors_blueprint)
app.register_blueprint(api_blueprint)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=25000)  # Запуск приложения
