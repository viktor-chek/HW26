from app import app


def test_api_one():
    """Тест типа данных"""
    response = app.test_client().get("/api/posts")
    assert isinstance(response.json, list), "Неверный тип данных"


def test_api_all_keys():
    """Тест на соответствие ключей"""
    posts_keys_names = {"poster_name", "poster_avatar",
                        "pic", "content", "views_count",
                        "likes_count", "pk"}
    response = app.test_client().get("/api/posts")

    assert len(response.json[0].keys()) == len(posts_keys_names), "Ошибка кол-ва ключей"


def test_api_two():
    """Тест типа данных"""
    response = app.test_client().get("/api/posts/1")
    assert type(response.json) == dict, "Не словарь"


def test_api_two_keys():
    """Тест на соответствие ключей"""
    posts_keys_names = {"poster_name", "poster_avatar",
                        "pic", "content", "views_count",
                        "likes_count", "pk"}
    response = app.test_client().get("/api/posts")

    assert len(response.json[0].keys()) == len(posts_keys_names), "Ошибка кол-ва ключей"
