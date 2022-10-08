from flask import Blueprint, jsonify
import logging
import utils


path = "data/data.json"


logger = logging.getLogger("API")           # Создание и настройка лога
logger.setLevel(logging.INFO)
file = logging.FileHandler("logs/api.log", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file.setFormatter(formatter)
logger.addHandler(file)


api_blueprint = Blueprint("api_blueprint", __name__, template_folder="templates")


@api_blueprint.route("/api/posts")  # Представление для api постов
def api_posts():
    content = utils.get_posts_all(path)
    logger.info("Запрос /api/posts")
    return jsonify(content)


@api_blueprint.route("/api/posts/<int:post_id>")   # Представление для api одного поста
def api_one_post(post_id):
    one_post = utils.get_post_by_pk(post_id)
    logger.info(f"Запрос /api/posts/{post_id}")
    return jsonify(one_post)

