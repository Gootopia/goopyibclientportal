"""
Simple example test script for connecting and subscribing to data
"""
from goopy_ibcp.clientportal_http import ClientPortalHttp
from goopy_ibcp.clientportal_websockets import ClientPortalWebsocketsBase
import json

"""
Interfacing with the IB Client Portal:
- If running IBeam, the watchdog is not required since IBeam will take care of pinging/re-authentication for you
"""
client_http = ClientPortalHttp(watchdog_start=False)
client_http.clientrequest_brokerage_accounts()
client_http.clientrequest_reauthenticate()
client_http.clientrequest_validate()
client_http.clientrequest_authentication_status()

# Example call to search by name or symbol
secdef=client_http.clientrequest_search("ES")
print(secdef.json[0])

# websocket for quote data
client_ws = ClientPortalWebsocketsBase()

try:
# loop forever in the client. Normally you do this in a worker thread as it runs perpetually to process messages
    client_ws.loop()
    print("Bye-Bye!")

except Exception as e:
    print(f"Exception: {e}")

finally:
    print("====ALL DONE====")

print("We be done!")
