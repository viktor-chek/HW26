from flask import Blueprint, render_template, jsonify

import utils
from db import db

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

data_json = "data/data.json"


@main_blueprint.route("/")  # Представление главной страницы
def main_page():
    all_posts = utils.get_posts_all(data_json)
    return render_template("index.html", data=all_posts)


@main_blueprint.route("/test_db")
def test_db():
    result = db.session.execute(
        "SELECT 222"
    ).scalar()

    return jsonify(
        {
            'result': result
        }
    )