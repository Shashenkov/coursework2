import logging
from flask import Blueprint, render_template, request, abort

from logger import create_logger
from app.posts.dao.postsdao import PostsDAO
from app.posts.dao.comments_dao import CommentsDAO


posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder="templates")
posts_dao = PostsDAO("data/posts.json")
comments_dao = CommentsDAO("data/comments.json")
create_logger()
logger = logging.getLogger("basic")


@posts_blueprint.route("/")
def posts_all():
    """Главная сраница: выводим все существующие посты.
    """
    logger.debug("Запрос всех постов.")
    posts = posts_dao.get_all_posts()
    return render_template("index.html", posts=posts)


@posts_blueprint.route("/posts/<int:post_pk>/")
def posts_one(post_pk):
    """Получаем пост по номеру, выводим соответствующие комментарии.
    Обрабатываем ValueError и ошибку 404, если пост отсутствует."""
    logger.debug(f"Запрос поста {post_pk}.")

    try:
        post = posts_dao.get_by_pk(post_pk)
        comments = comments_dao.get_comments_by_post_id(post_pk)
    except ValueError as error:
        logger.debug('ValueError')
        return render_template("error.html", error=error)
    else:
        if post is None:
            abort(404)
        number_of_comments = len(comments)

        return render_template("post.html", post=post, comments=comments, number_of_comments=number_of_comments)


@posts_blueprint.errorhandler(404)
def post_error(e):
    logger.debug("Пост не найден. error404")
    return "Пост не найден.", 404


@posts_blueprint.route("/search/")
def posts_search():
    """Выводим пост по вхождению ключевого слова в текст поста.
    """
    query = request.args.get("s", None)
    logger.debug(f"Поиск выполняется по вхождению ключевого слова '{query}'")
    if query != "":
        posts = posts_dao.search(query)
        number_of_posts = len(posts)
    else:
        posts = []
        number_of_posts = 0

    return render_template("search.html", query=query, posts=posts, number_of_posts=number_of_posts)


@posts_blueprint.route("/users/<username>")
def posts_by_user(username):
    """Выводим пост конкретного пользователя.
     Выводим тот пост, у которого poster-name соответствует username из запроса.
     """
    posts = posts_dao.get_by_user(username)
    logger.debug(f"Поиск постов по пользователю'{username}'")
    number_of_posts = len(posts)
    return render_template("user-feed.html", posts=posts, number_of_posts=number_of_posts)
