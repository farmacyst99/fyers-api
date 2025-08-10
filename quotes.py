from fyers_apiv3 import fyersModel
import os


client_id = os.getenv("FYERS_CLIENT_ID")
access_token = os.getenv("FYERS_ACCESS_TOKEN")

# Initialize the Fyers API client
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False)

data = {
    "symbols":"MCX:NATURALGAS25AUGFUT"
}

response = fyers.quotes(data=data)
print(response)
