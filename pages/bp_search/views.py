from flask import Blueprint, render_template, request
import utils

search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")

data_json = "data/data.json"


@search_blueprint.route("/search")    # Представление страницы поиска
def search_page():
    search = request.args.get("s")
    search_posts = utils.search_for_posts(search)
    return render_template("search.html", posts=search_posts)

