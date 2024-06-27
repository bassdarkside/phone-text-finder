import json
from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    flash,
    jsonify,
    url_for,
)
from flask import current_app as app
from flask_login import login_required, current_user
from .utils.utils import main_search
from .models import Data, Phone, User
from .extensions import db
from .enums import CountryCode
from .forms import PhoneCodeForm
from .utils.validators import PhoneExists


views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    form = PhoneCodeForm()
    if form.validate_on_submit():
        input_number = "".join(filter(str.isdigit, form.input_number.data))
        country_code = str(CountryCode[form.code.data].value)
        phone_exists = PhoneExists()
        exists = phone_exists(
            input_number,
            country_code,
            current_user.id,
        )

        if exists is False:
            app.logger.warning("Phone number %s already exists", input_number)
            flash("This number is already exist", category="warning")
            return render_template(
                "home.html",
                user=current_user,
                codes=CountryCode,
                form=form,
            )
        data = main_search(country_code, input_number)
        if not data:
            app.logger.warning(
                "No data found for phone number %s", input_number
            )
            flash("No data found", category="error")
        if data:
            new_phone = Phone(
                phonenumber=input_number,
                country_code=country_code,
                user_id=current_user.id,
            )
            db.session.add(new_phone)
            db.session.commit()
            for item in [f"{i[0]}\n" for i in data]:
                if not item:
                    continue
                new_data = Data(
                    data=item,
                    phone_num_id=new_phone.id,
                )
                db.session.add(new_data)
            db.session.commit()
            app.logger.info("Phone number %s added successfully", input_number)
            flash("Phone number added successfully", category="success")
    return render_template(
        "home.html",
        user=current_user,
        codes=CountryCode,
        form=form,
    )


@views.route("delete-number", methods=["POST"])
@login_required
def delete_phonenumber():
    data = json.loads(request.data)
    phone = Phone.query.get(data["numberId"])
    if phone:
        if phone.user_id == current_user.id:
            db.session.delete(phone)
            db.session.commit()

            app.logger.info(
                "Phone number %s deleted successfully", phone.phonenumber
            )
            flash("Phone number has been deleted", category="success")
    return jsonify({})


@views.route("delete-user")
@login_required
def delete_user_account():
    user = User.query.get(current_user.id)
    if user:
        db.session.delete(user)
        db.session.commit()
        app.logger.info("User %s deleted successfully", user.username)
        flash("Your account has been deleted", category="success")
    return redirect(url_for("views.home"))
