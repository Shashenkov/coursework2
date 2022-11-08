from run import app


class TestAPI:
    """Класс тестов к API
    """
    # Тестируем все посты.
    def test_app_all_posts_status_code(self):
        """Проверяем статус код"""
        response = app.test_client().get("/api/posts", follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"
        assert response.mimetype == "application/json", "Получен не JSON"

    def test_app_all_posts_type_count_content(self):
        """Проверяем получены ли верные данные."""
        response = app.test_client().get("/api/posts", follow_redirects=True)
        assert type(response.json) == list, "Получен не список"
        assert len(response.json) == 8, "Получено неверное количество элементов в списке"

    def test_app_all_posts_mimetype(self):
        """Проверяем получен ли JSON"""
        response = app.test_client().get("/api/posts", follow_redirects=True)
        assert response.mimetype == "application/json", "Получен не JSON"

    def test_app_all_posts_type_check_keys(self):
        """Проверяем совпадают ли полученные ключи."""
        keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
        response = app.test_client().get("/api/posts", follow_redirects=True)
        first_keys = set(response.json[0].keys())
        assert keys == first_keys, "Полученные ключи не совпадают."

    # Тестируем один пост.

    def test_app_one_post_status_code(self):
        """Проверяем статус код"""
        response = app.test_client().get("/api/posts/1", follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"

    def test_app_one_post_type(self):
        """Проверяем получен ли словарь."""
        response = app.test_client().get("/api/posts/1", follow_redirects=True)
        assert type(response.json) == dict, "Получен не словарь"

    def test_app_one_post_mimetype(self):
        """Проверяем получен ли JSON"""
        response = app.test_client().get("/api/posts/1", follow_redirects=True)
        assert response.mimetype == "application/json", "Получен не JSON"