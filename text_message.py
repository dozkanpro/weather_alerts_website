from twilio.rest import Client
import os

account_sid = os.environ.get("OWN_ACCOUNT_SID")
auth_token = os.environ.get("OWN_AUTH_TOKEN")


class Message:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_text_message(self, weather, phone_number):
        message = self.client.messages \
            .create(
            body=weather,
            from_="+12057400183",
            to=phone_number
        )
