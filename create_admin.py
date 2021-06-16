from getpass import getpass
import sys

from webapp import db, create_app
from webapp.model import User


app = create_app()

with app.app_context():
    user_name = input("Введите имя: ")

    if User.query.filter(User.user_name == user_name).count():
        print("Пользователь с таким именем уже существует")
        sys.exit(0)

    password_first = getpass("Введите пароль: ")
    password_repeat = getpass("Повторите пароль: ")

    if not password_first == password_repeat:
        print("Пароли не совпадают")
        sys.exit(0)

    new_user = User(user_name=user_name, role="admin")
    new_user.set_password(password_first)


    db.session.add(new_user)
    db.session.commit()
    print(f"Создан пользователь с id={new_user.id}")
