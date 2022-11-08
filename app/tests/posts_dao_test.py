import pytest

from app.posts.dao.postsdao import PostsDAO


class TestPostsDAO:
    """ Класс тестов к posts_dao.py
    """
    @pytest.fixture
    def posts_dao(self):
        return PostsDAO("data/posts.json")

    @pytest.fixture
    def keys_expected(self):
        return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    def test_get_all_posts_check_type(self, posts_dao):
        posts = posts_dao.get_all_posts()
        assert type(posts) == list, "Результат поиска должен быть списком."
        assert type(posts[0]) == dict, "Элемент поиска должен быть словарём."

    def test_get_all_has_keys(self, posts_dao, keys_expected):
        posts = posts_dao.get_all_posts()
        for post in posts:
            keys = post.keys()
            assert set(keys) == keys_expected, "Полученные ключи неверны."

    def test_get_by_pk_chech_type(self, posts_dao):
        post = posts_dao.get_by_pk(1)
        assert type(post) == dict, "Элемент поиска должен быть словарём."

    def test_get_by_pk_has_keys(self, posts_dao, keys_expected):
        post = posts_dao.get_by_pk(1)
        keys = post.keys()
        assert set(keys) == keys_expected, "Полученные ключи неверны."

    parametrize_to_get_by_pk = [1, 2, 3, 4, 5, 6, 7, 8]

    @pytest.mark.parametrize("post_pk", parametrize_to_get_by_pk)
    def test_get_by_correct_pk(self, posts_dao, post_pk):
        post = posts_dao.get_by_pk(post_pk)
        assert post["pk"] == post_pk, "Номер поста не соответствует."


    def test_get_by_user_chech_type(self, posts_dao):
        posts = posts_dao.get_by_user("leo")
        assert type(posts) == list, "Результат поиска должен быть списком."
        assert type(posts[0]) == dict, "Элемент поиска должен быть словарём"

    def test_get_by_user_has_keys(self, posts_dao, keys_expected):
        post = posts_dao.get_by_user("leo")[0]
        post_keys = set(post.keys())
        assert post_keys == keys_expected, "Полученные ключи неверны."


    parameters_to_get_by_user = [
        ("leo", [1,5]),
        ("hank", [3,7]),
        ]

    @pytest.mark.parametrize("user_name, post_pks", parameters_to_get_by_user)
    def test_get_by_user_correct_match(self, posts_dao, user_name, post_pks):
        posts = posts_dao.get_by_user(user_name)
        pks = []
        for post in posts:
            pks.append(post["pk"])
        assert pks == post_pks, f"Неверный список постов для пользователя {user_name}"

    def test_searh_chech_type(self, posts_dao):
        posts = posts_dao.search("а")
        assert type(posts) == list, "Результат поиска должен быть списком."
        assert type(posts[0]) == dict, "Элемент поиска должен быть словарём"

    def test_search_has_keys(self, posts_dao, keys_expected):
        post = posts_dao.search("а")[0]
        post_keys = set(post.keys())
        assert post_keys == keys_expected, "Полученные ключи неверны."

    queries_and_responses = [
        ("а", list(range(1, 8 + 1)))
    ]

    @pytest.mark.parametrize("query, post_pks", queries_and_responses)
    def test_search_correct_match(self, posts_dao, query, post_pks):

        posts = posts_dao.search(query)
        pks = []
        for post in posts:
            pks.append(post["pk"])
        assert pks == post_pks, f"Неверный поиск по запросу {query}"
