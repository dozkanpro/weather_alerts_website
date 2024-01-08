from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField, StringField
from wtforms.validators import DataRequired, ValidationError
import phonenumbers
from weather import Weather
from text_message import Message
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY_WEATHER')
Bootstrap5(app)


class LocationForm(FlaskForm):
    lat = DecimalField('Latitude:', places=6, rounding=False)
    long = DecimalField('Longitude:', places=6, rounding=False)
    submit = SubmitField()


class PhoneForm(FlaskForm):
    phone = StringField('Phone', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_phone(self, phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')


@app.route('/', methods=['GET', 'POST'])
def home():
    location_form = LocationForm()
    if location_form.validate_on_submit():
        lat = location_form.lat.data
        long = location_form.long.data
        current_weather = Weather(lat, long).get_weather_forecast()
        return render_template("index.html", location_form=location_form, current_weather=current_weather)
    return render_template("index.html", location_form=location_form)


@app.route("/send-message/<string:current_weather>", methods=['GET', 'POST'])
def send_message(current_weather):
    phone_form = PhoneForm()
    if phone_form.validate_on_submit():
        phone_number = phone_form.phone.data
        Message().send_text_message(current_weather, phone_number)
        return redirect(url_for('home'))
    return render_template("send-message.html", form=phone_form)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
