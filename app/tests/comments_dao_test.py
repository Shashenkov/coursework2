import pytest

from app.posts.dao.comments_dao import CommentsDAO


class TestCommentsDAO:
    """ Класс тестов к comments_dao.py.
    """
    @pytest.fixture
    def comments_dao(self):
        return CommentsDAO("app/tests/mock/comments.json")

    @pytest.fixture
    def keys_expected(self):
        return {"post_id", "commenter_name", "comment", "pk"}

    def test_get_comments_by_post_id_check_type(self, comments_dao):
        comments = comments_dao.get_comments_by_post_id(1)
        assert type(comments) == list, "Результат поиска должен быть списком."
        assert type(comments[0]) == dict, "Элемент поиска должен быть словарём"

    def test_get_comments_by_post_id_check_keys(self, comments_dao, keys_expected):
        comment = comments_dao.get_comments_by_post_id(1)[0]
        comment_keys = set(comment.keys())
        assert comment_keys == keys_expected, "Полученные ключи неверны."

    parameters_to_get_comments_by_post_id = [
        (1, {1, 2}),
        (2, {7}),
        (0, set())
    ]

    @pytest.mark.parametrize("post_id, correct_comments_pks", parameters_to_get_comments_by_post_id)
    def test_get_comments_by_post_id_check_match(self, comments_dao, post_id, correct_comments_pks):
        comments = comments_dao.get_comments_by_post_id(post_id)
        comment_pks = set([comment["pk"] for comment in comments])
        assert comment_pks == correct_comments_pks, f"Не совпадает pk комментов для поста {post_id}"
