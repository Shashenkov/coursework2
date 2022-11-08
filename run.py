import logging
from flask import Flask

from logger import create_logger
from app.posts.views import posts_blueprint
from app.api.views import api_blueprint

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)

create_logger()
logger = logging.getLogger("basic")


@app.errorhandler(404)
def page_is_absent(e):
    """Возвращаем статус-код 404 в случае запроса несуществующей страницы.
    """
    logger.debug("error404")
    return "Страница не сущестует", 404


@app.errorhandler(500)
def internal_server_error(e):
    """Возвращаем статус-код 500 на случай проблемы с сервером.
    """
    logger.debug("error500")
    return "внутренняя проблема сервера", 500


if __name__ == "__main__":
    app.run(debug=True, port=1004)
