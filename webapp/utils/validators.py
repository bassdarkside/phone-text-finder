from wtforms.validators import ValidationError

from webapp.models import Phone


class Unique(object):
    def __init__(self, model, field, message="This element already exists."):
        self.model = model
        self.field = field

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)


class PhoneExists(object):
    def __init__(self):
        self.message = "Phone number already exists"
        self.model = Phone()
        self.valid = False

    def __call__(self, phone, code, user_id):
        check = self.model.query.filter_by(
            phonenumber=phone, country_code=code, user_id=user_id
        ).first()
        if check:
            self.valid = False
            return self.valid


class PhoneFormat(object):
    def __init__(self):
        self.message = "Format phone number is not correct"

    def __call__(self, code, number):
        if isinstance(number, str) and number.isdigit() is False:
            raise ValidationError(self.message)

        if (
            code == "UA"
            or code == "PL"
            or code == "EE"
            or code == "LV"
            or code == "LT"
        ):
            if len(number) != 9:
                raise ValidationError(self.message)
        if code == "US":
            if len(number) != 10:
                raise ValidationError(self.message)
