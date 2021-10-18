from flask_wtf import FlaskForm
from wtforms import (BooleanField, IntegerField, PasswordField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from webapp.user.models import User


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
        validators=[DataRequired(), EqualTo("password")],
        render_kw={"class": "form-control"},
    )

    submit = SubmitField(
        "Зарегистрироваться",
        render_kw={"class": "btn btn-primary"},
    )

    def validate_user_name(self, user_name):
        user_count = User.query.filter_by(user_name=user_name.data).count()
        if user_count > 0:
            raise ValidationError("Пользователь с таким именеем уже существует!")

    def validate_email(self, email):
        email_count = User.query.filter_by(email=email.data).count()
        if email_count > 0:
            raise ValidationError("Пользователь с таким E-mail уже существует!")
