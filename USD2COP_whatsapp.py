import os
from polygon import RESTClient
from twilio.rest import Client

client = RESTClient(api_key=os.environ["POLYGON_API_KEY"])

last_close = client.get_previous_close_agg(
                    "C:USDCOP",
)
print(last_close)

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

from_whatsapp_number='whatsapp:+14155238886'
to_whatsapp_numbre='whatsapp:+573007536533'

client.messages.create(body=last_close,
                       from_=from_whatsapp_number,
                       to=to_whatsapp_numbre)