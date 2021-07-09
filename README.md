# Web Track

## 1) Виртуальное окружение в Windows:

### env/Scripts/activate

## 2) Сервера Flask из VSCode в Windows 10:

# $env:FLASK_APP="webapp"
# $env:FLASK_ENV="development"
# $env:FLASK_DEBUG=1
# python -m flask run

## 3) Миграции:

#### $env:FLASK_APP="webapp" | flask db init

#### move webapp.db webapp.db.old

### Создание миграции:

#### $env:FLASK_APP="webapp"
#### flask db migrate -m "users and news table"

#### flask db stamp <Revision ID>
