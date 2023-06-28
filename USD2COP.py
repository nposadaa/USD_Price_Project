import os
import re
from polygon import RESTClient
from datetime import date

today = date.today()
date = today.strftime("%m/%d/%Y")
client = RESTClient(api_key=os.environ["POLYGON_API_KEY"])

PreviousCloseAgg = client.get_previous_close_agg(
                    "C:USDCOP",
)
# print(f"""The original value is:
      
# {PreviousCloseAgg}
# """)

# We convert the return to  string
PreviousCloseAgg_STR = str(PreviousCloseAgg[0])

#We search for the word close, establish it start index, and its lenght, then print the message.
word = "close"
lword = len(word)
start_index = re.search(word, PreviousCloseAgg_STR).start()
close_value = PreviousCloseAgg_STR[start_index + lword + 1:start_index + lword + 5]
print(f"The closing value of 1 USD in COP is {close_value} for {date}. This is a service by Nico Posada!")