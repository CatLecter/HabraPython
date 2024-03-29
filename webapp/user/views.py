from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user

import webapp
from webapp.db import db
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User

blueprint = Blueprint("user", __name__, url_prefix="/users")


@blueprint.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("news.index"))
    title = "Авторизация"
    login_form = LoginForm()
    return render_template(
        "user/login.html",
        page_title=title,
        form=login_form,
    )


@blueprint.route("/process-login", methods=["POST"])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.user_name == form.user_name.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash("Вы успешно вошли на сайт")
            return redirect(url_for("news.index"))

    flash("Неправильно введены логин или пароль")
    return redirect(url_for("user.login"))


@blueprint.route("/logout")
def logout():
    logout_user()
    flash("Вы вышли из провиля")
    return redirect(url_for("news.index"))


@blueprint.route("/reg")
def reg():
    if current_user.is_authenticated:
        return redirect(url_for("news.index"))
    title = "Регистрация"
    login_form = RegistrationForm()
    return render_template(
        "user/reg.html",
        page_title=title,
        form=login_form,
    )


@blueprint.route("/process_reg", methods=["POST"])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            user_name=form.user_name.data,
            email=form.email.data,
            age=form.age.data,
            role="user",
        )
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash("Вы успешно зарегистрировались!")
        return redirect(url_for("user.login"))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Ошибка в поле {getattr(form, field).label.text}: - {error}")
        return redirect(url_for("user.reg"))
