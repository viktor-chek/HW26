import json

data_json = "data/data.json"
data_comments = "data/comments.json"


def get_posts_all(data):
    """Возвращает список всех постов"""
    with open(data, encoding="utf-8") as f:
        all_data = json.load(f)
        return all_data


def get_post_by_pk(pk):
    """Возвращает пост по его pk"""
    data = get_posts_all(data_json)
    for item in data:
        if item["pk"] == pk:
            return item


def get_comments_by_post_id(post_id):
    """Возвращает комментарии по id поста. Поднимает ошибку если поста не существует"""
    with open(data_comments, encoding="utf-8") as f:
        data = json.load(f)
    posts = get_posts_all(data_json)
    result = []
    count_posts = []
    for item in posts:
        count_posts.append(item["pk"])
    if post_id in count_posts:
        for f in data:
            if post_id == f["post_id"]:
                result.append(f)
    else:
        raise ValueError("Такого поста нет")
    return result


def search_for_posts(query):
    posts = get_posts_all(data_json)
    result = []
    for item in posts:
        if str(query) in item["content"]:
            result.append(item)
    return result


def get_posts_by_user(user_name):
    """Возвращает посты конкретного пользователя, вызывает ошибку если пользователь не найден"""
    posts = get_posts_all(data_json)
    result = []
    for item in posts:
        if user_name == item["poster_name"]:
            result.append(item)
    if len(result) > 0:
        return result
    else:
        raise ValueError("Такого пользователя не существует")
