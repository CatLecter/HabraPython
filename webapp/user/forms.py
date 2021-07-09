from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    user_name = StringField(
        "Имя пользователя",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )

    password = PasswordField(
        "Пароль",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )

    remember_me = BooleanField(
        "Запомнить меня",
        default=True,
        render_kw={"class": "form-check-input"},
    )

    submit = SubmitField(
        "Отправить",
        render_kw={"class": "btn btn-primary"},
    )

class RegistrationForm(FlaskForm):
    user_name = StringField(
        "Имя пользователя",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )

    email = StringField(
        "E-mail",
        validators=[DataRequired(), Email()],
        render_kw={"class": "form-control"},
    )

    age = IntegerField(
        "Возраст",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )

    password = PasswordField(
        "Пароль",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )

    password_repeat = PasswordField(
        "Повтроите пароль",
        validators=[DataRequired(), EqualTo('password')],
        render_kw={"class": "form-control"},
    )

    submit = SubmitField(
        "Зарегистрироваться",
        render_kw={"class": "btn btn-primary"},
    )
