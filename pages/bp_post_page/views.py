from flask import Blueprint, render_template
import utils

post_blueprint = Blueprint("post_blueprint", __name__, template_folder="templates")


@post_blueprint.route("/post/<int:pk>", methods=["GET"])  # Представление отдельного поста
def post_page(pk):
    get_post = utils.get_post_by_pk(pk)
    get_comments = utils.get_comments_by_post_id(pk)
    return render_template("post.html", post=get_post, comment=get_comments)
