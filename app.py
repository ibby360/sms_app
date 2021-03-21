from twilio.rest import Client
from cred.credentials import (my_account_sid,
                              my_auth_token,
                              my_telephone,
                              my_service_telephone
)

account_sid = my_account_sid
auth_token = my_auth_token
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body='Hi there, how was your day?',
        from_=my_telephone,
        to=my_service_telephone
    )

print(message.sid)
