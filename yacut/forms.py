from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

PATTERN_SHORT_URL = r'^[A-Za-z0-9_]+$'
START_LENGHT_NUMBER = 1
END_LENGHT_NUMBER = 16


class СutForm(FlaskForm):
    original_link = URLField(
        'Ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    URL(require_tld=True, message='Неверная ссылка')]
    )
    custom_id = URLField(
        'Укороченная ссылка',
        validators=[
            Length(START_LENGHT_NUMBER, END_LENGHT_NUMBER,
                   message='количество символов не может быть более 16'),
            Optional(),
            Regexp(PATTERN_SHORT_URL,
                   message='Указаны недопустимые символы')
        ]
    )
    submit = SubmitField('Создать')