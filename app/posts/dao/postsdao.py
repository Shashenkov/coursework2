from flask import json


class PostsDAO:
    """ Класс ответственный за работу со всеми постами.
    """
    def __init__(self, path):
        self.path = path

    def _load(self):
        with open(f"{self.path}", "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_all_posts(self):
        """ Возвращает все посты.
        """
        return self._load()

    def get_by_pk(self, pk):
        """ Возвращает пост по идентификатору.
        """
        posts = self.get_all_posts()
        for post in posts:
            if post["pk"] == pk:
                return post

    def get_by_user(self, user_name):
        """ Получаем пост конкретного пользователя.
        Получаем тот пост, у которого poster-name соответствует username из запроса.
        """
        posts = self.get_all_posts()
        posts_by_user = []

        for post in posts:
            if post["poster_name"] == user_name:
                posts_by_user.append(post)
        return posts_by_user

    def search(self, query):
        """Получаем пост по вхождению ключевого слова в текст поста.
        """
        posts = self.get_all_posts()
        matching_posts = []
        query_lower = query.lower()

        for post in posts:
            if query_lower in post["content"].lower():
                matching_posts.append(post)
        return matching_posts
