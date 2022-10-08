from flask import Blueprint, render_template
import utils

user_blueprint = Blueprint("user_blueprint", __name__, template_folder="template")


@user_blueprint.route("/user/<name>")  # Представление постов конкретного пользователя
def user_page(name):
    user = utils.get_posts_by_user(name)
    return render_template("user_feed.html", user=user)
