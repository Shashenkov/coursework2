from flask import Blueprint, jsonify
import logging

from logger import create_logger
from app.posts.dao.postsdao import PostsDAO
from app.posts.dao.comments_dao import CommentsDAO


api_blueprint = Blueprint("api_blueprint", __name__)
posts_dao = PostsDAO("data/posts.json")
comments_dao = CommentsDAO("data/comments.json")
create_logger()
logger = logging.getLogger("basic")


@api_blueprint.route("/api/posts/")
def posts_all():
    """Возвращает полный список постов в виде JSON-списка.
    """
    logger.debug("Запрошены все посты через api.")
    posts = posts_dao.get_all_posts()
    return jsonify(posts)


@api_blueprint.route("/api/posts/<int:post_pk>/")
def posts_one(post_pk):
    """Возвращает один пост в виде JSON-словаря.
    """
    logger.debug(f"Запрошен пост с pk {post_pk} через API")
    post = posts_dao.get_by_pk(post_pk)
    return jsonify(post)
