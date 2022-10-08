from flask import Blueprint


errors_blueprint = Blueprint("errors_blueprint", __name__)


@errors_blueprint.app_errorhandler(500)
def page_not_found(e):                      # Обработка ошибки 500
    return """
    <link href="/static/css/styles.min.css" rel="stylesheet">   
    <h1 align="center"> 500 </h1>
    <h2 align="center"> Ошибка сервера </h2>
    """, 500


@errors_blueprint.app_errorhandler(404)                      # Обработка ошибки 404
def page_not_found(e):
    return """
    <link href="/static/css/styles.min.css" rel="stylesheet">
    <h1 align="center"> 404 </h1>
    <h2 align="center"> Страница не найдена </h2>
    """, 404
