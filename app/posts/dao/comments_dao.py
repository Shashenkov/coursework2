from flask import json


class CommentsDAO:
    """Класс, отвечающий за работу с данными по коментариям.
    """
    def __init__(self, path):
        self.path = path

    def _load_comments(self):
        """ Загружаем комментарии.
        """
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_comments_by_post_id(self, post_pk):
        """ Получаем комментарии к соответствующему посту.
        """
        comments = self._load_comments()
        comments_by_id = []
        for comment in comments:
            if comment["post_id"] == post_pk:
                comments_by_id.append(comment)
        return comments_by_id
