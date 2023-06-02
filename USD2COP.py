import os
from polygon import RESTClient

client = RESTClient(api_key=os.environ["POLYGON_API_KEY"])

last_close = client.get_previous_close_agg(
                    "C:USDCOP",
)
print(last_close)