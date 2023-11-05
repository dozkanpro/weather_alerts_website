from twilio.rest import Client
import os

account_sid = os.environ.get("OWN_ACCOUNT_SID")
auth_token = os.environ.get("OWN_AUTH_TOKEN")


class Message:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_text_message(self, weather, phone_number):
        validation_request = self.client.validation_requests \
            .create(
            friendly_name='My Phone Number',
            phone_number=phone_number
        )
        message = self.client.messages \
            .create(
            body=weather,
            from_="my_phone",
            to=phone_number
        )
