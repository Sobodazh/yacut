# Cервис YaCut

### Описание
Проект YaCut — это сервис укорачивания ссылок. Его назначение — совмещать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.
Интерфейс сервиса — одна страница с формой.

### Технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=043A6B)](https://www.sqlalchemy.org/)
[![Flask](https://img.shields.io/badge/-Flask-464646?style=flat&logo=Flask&logoColor=ffffff&color=043A6B)](https://flask.palletsprojects.com/en/2.3.x/)
[![REST](https://img.shields.io/badge/-REST-464646?style=flat&logo=REST&logoColor=ffffff&color=043A6B)](https://python-rest-framework.readthedocs.io/en/latest/)

## Запуск проекта
```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Создайте файл .env в корневой директории со следующим содержимым:
```
FLASK_APP=
FLASK_ENV=
DATABASE_URI=
SECRET_KEY=
```
Запустите проект
```
flask run
```
После запуска, проект будет доступен по адресу http://localhost/

## API
API проекта доступен всем желающим. Сервис обслуживает только два эндпоинта:
* /api/id/ — POST-запрос на создание новой короткой ссылки;
* /api/id/<short_id>/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

## Примеры запросов

**GET** `.../api/id/{short_id}/`
*200*
```
{
  "url": "string"
}
```
*404*
```
{
  "message": "Указанный id не найден"
}
```

**POST** `.../api/id/`
```
{
  "url": "string",
  "custom_id": "string"
}
```
*201*
```
{
  "url": "string",
  "short_link": "string"
}
```
*400*
```
{
  "message": "Отсутствует тело запроса"
}
```

### Автор
Сободаж Антон
