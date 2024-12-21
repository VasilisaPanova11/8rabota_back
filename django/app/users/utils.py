import redis
from app.settings import REDIS_HOST, REDIS_PORT

KEY_USERNAME = "username"
KEY_THEME = "theme"
KEY_LANG = "lang"

THEME_CHOICES = [("light", "Светлая тема"), ("dark", "Темная тема")]
DEFAULT_THEME = 0

LANG_CHOICES = [("RU", "Русский"), ("EN", "Английский")]
DEFAULT_LANG = 0


def connect() -> redis.Redis:
    return redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


def get_data(username):
    rdb = connect()
    theme = rdb.hget(username, KEY_THEME)
    lang = rdb.hget(username, KEY_LANG)
    if theme is None:
        theme = THEME_CHOICES[DEFAULT_THEME][0]
        lang = LANG_CHOICES[DEFAULT_LANG][0]
    return theme, lang


def check_cookie(request):
    return request.COOKIES.get(KEY_USERNAME, False)


def set_cookie(request, response, max_age):
    username = request.user.username
    theme, lang = get_data(username)
    response.set_cookie(KEY_USERNAME, username, max_age=max_age)
    response.set_cookie(KEY_THEME, theme, max_age=max_age)
    response.set_cookie(KEY_LANG, lang, max_age=max_age)


def get_cookie_data(request):
    username = request.COOKIES.get(KEY_USERNAME, None)
    theme = request.COOKIES.get(KEY_THEME, None)
    lang = request.COOKIES.get(KEY_LANG, None)
    return {"username": username, "theme": theme, "lang": lang}


def save_user_data(username, theme, lang):
    rdb = connect()
    rdb.set(KEY_USERNAME, username)
    rdb.hset(username, KEY_THEME, theme)
    rdb.hset(username, KEY_LANG, lang)
