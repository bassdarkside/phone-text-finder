from flask import (
    Blueprint,
    render_template,
    flash,
    redirect,
    url_for,
)
from flask import current_app as app
from flask_login import login_user, login_required, logout_user, current_user
from .forms import EmailUsernamePasswordForm, EmailPasswordForm
from .models import User
from .extensions import db


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = EmailPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first_or_404()
        if user.is_correct_password(form.password.data):
            if login_user(user):
                app.logger.info("%s logged in successfully", user)
                flash("Logged in successfully!", category="success")
                return redirect(url_for("views.home"))
        else:
            flash("Incorrect password. Try again", category="error")
            app.logger.warning(
                "Incorrect password for %s", user, exc_info=True
            )
            return redirect(url_for("auth.login"))
    return render_template("login.html", user=current_user, form=form)


@auth.route("/logout")
@login_required
def logout():
    if logout_user():
        app.logger.info("%s logged out", current_user)
        flash("Logged out successfully!", category="success")
    return redirect(url_for("auth.login"))


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    form = EmailUsernamePasswordForm()
    email = form.email.data
    password = form.password.data
    password2 = form.password2.data
    if password != password2:
        app.logger.warning(
            "Passwords don't match for %s", email, exc_info=True
        )
        flash("Passwords don't match.", category="error")
    if form.validate_on_submit():
        new_user = User(
            email=email,
            password=password,
            username=form.username.data,
        )
        db.session.add(new_user)
        db.session.commit()

        app.logger.info("%s account created!", new_user)
        flash("Account created!", category="success")

        if login_user(new_user, remember=True):
            app.logger.info("%s logged in successfully", new_user)
            return redirect(url_for("views.home"))

    return render_template("sign_up.html", user=current_user, form=form)
