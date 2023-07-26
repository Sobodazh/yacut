from http import HTTPStatus as status
from re import match

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap, get_unique_short_id


PATTERN_URL = r'^[a-z]+://[^\/\?:]+(:[0-9]+)?(\/.*?)?(\?.*)?$'
PATTERN_SHORT = r'^[A-Za-z0-9_]{1,16}$'


@app.route('/api/id/<string:short>/', methods=['GET'])
def cut_redirect_api(short):
    redirect_url = URLMap.query.filter_by(short=short).first()
    if not redirect_url:
        raise InvalidAPIUsage('Указанный id не найден', status.NOT_FOUND)
    return jsonify({'url': redirect_url.original})


@app.route('/api/id/', methods=['POST'])
def short_url_api():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if not match(PATTERN_URL, data['url']):
        raise InvalidAPIUsage('Указаны недопустимые символы')
    if not data.get('custom_id'):
        data['custom_id'] = get_unique_short_id()
    elif URLMap.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPIUsage(f'Имя "{data["custom_id"]}" уже занято.')
    elif not match(PATTERN_SHORT, data['custom_id']):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), status.CREATED