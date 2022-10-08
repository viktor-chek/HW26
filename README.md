
# Курсовая работа 3

#### Для запуска:

    1. Скачать
    2. Установить зависимости (pip install -r requirements.txt)
    3. Запустить проект (python app.py)

Приложение работает по адресу http://127.0.0.1:5000

#### Главная страница:

`url = "/"`

![image](https://i120.fastpic.org/big/2022/0612/0d/e2b5392ce8dfd5d7fe18110aa5ee550d.png?md5=Wg7GXl4q972ShlBQPw8hig&expires=1655020800)

Страница отоброжающая все посты. В правом верхнем углу поиск

---
#### Страница поста:

`url = "/post/<post_id>"`

![image](https://i120.fastpic.org/big/2022/0612/d5/e700983b6b1e827b68d819aee401f6d5.png?md5=MWusAOagCYjvOYX93o3TmQ&expires=1655020800)

Страница поста. Текст поста, просмотры, комментарии

---
#### Страница поиска:

`url = "/search"`

![image](https://i120.fastpic.org/big/2022/0612/d1/47e1206f9e56f5df80412313b06e42d1.png?md5=S9O5QwbtclBce_laHVu4-Q&expires=1655020800)

Поиск поста по введенной строке

---
#### Страница пользователя:

![image](https://i120.fastpic.org/big/2022/0612/78/3d3eea4cbb9c0be2fab7d46186d0c678.png?md5=SnHWuCA5X1NA49lMlBmu9w&expires=1655020800)

Выводится при нажатии на аватарку или имя пользователя. Показывает все существующие у него посты.

---
Обращение к api производятся по адресам:
`"/api/posts"`
и
`"/api/posts/<post_id>"`

Все обращения записываются в файл 
- logs/api.log
