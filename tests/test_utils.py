import utils

testing_data_json = "tests/testing_json.json"

path = utils.get_posts_all(testing_data_json)

# Тесты функции get_posts_all


def test_get_all_posts():
    """Тест типа данных"""
    assert type(path) is list, "Не верный тип данных"


def test_dict():
    """Тест на соответствие ключей"""
    waiting_keys = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]
    post = path[0]
    assert type(post) is dict, "Не словарь"

    post_keys = []
    for item in post.keys():
        post_keys.append(item)
    assert waiting_keys == post_keys, "Не хватает ключей"


# Тест функции get_posts_by_user


def test_get_posts_by_user():
    """Тест типа данных"""
    test_name = path[0]["poster_name"]
    user_result = utils.get_posts_by_user(test_name)
    assert type(user_result) is list, "Возвращается не список"


# Тесты функции get_comments_by_post_id


def test_get_comments_by_post_id():
    """Тест типа данных и соответствие ключей"""
    test_id = path[0]["pk"]
    comments_of_user = utils.get_comments_by_post_id(test_id)

    assert type(comments_of_user) is list, "Возвращается не список"

    waiting_keys = ["post_id", "commenter_name", "comment", "pk"]
    post_keys = []

    for item in comments_of_user[0].keys():
        post_keys.append(item)

    assert post_keys == waiting_keys, "Не хватает ключей"


# Тест функции search_for_posts


def test_search_for_posts():
    """Тест типа данных"""
    test_str = "Питонист"
    search = utils.search_for_posts(test_str)

    assert type(search) is list, "Возвращается не список"


# Тест функции get_post_by_pk


def test_get_post_by_pk():
    """Тест типа данных"""
    post_pk = path[0]["pk"]
    result = utils.get_post_by_pk(post_pk)

    assert type(result) is dict, "Возвращается не словарь"
