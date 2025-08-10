from fyers_apiv3 import fyersModel

with open("fyers_client_id.txt", "r") as f:
    client_id = f.read().strip()

with open("fyers_access_token.txt", "r") as f:
    access_token = f.read().strip()


# Live Market Data
fyers = fyersModel.FyersModel(client_id=client_id,log_path="logs/", token=access_token)

data = {
    "symbols":"MCX:NATURALGAS25AUGFUT"
}

response = fyers.quotes(data=data)
#print(response)


if response and response.get('s') == 'ok' and response.get('d'):
    symbol_data = response['d'][0]
    name_of_symbol = symbol_data.get('n', 'N/A')
    LTP = symbol_data.get('v', {}).get('lp', 'N/A')
    change_in_price = symbol_data.get('v', {}).get('ch', 'N/A')
    open_price = symbol_data.get('v', {}).get('open_price', 'N/A')
    high_price = symbol_data.get('v', {}).get('high_price', 'N/A')
    low_price = symbol_data.get('v', {}).get('low_price', 'N/A')
    prev_close_price = symbol_data.get('v', {}).get('prev_close_price', 'N/A')
    volume = symbol_data.get('v', {}).get('volume', 'N/A')


    print(f"Symbol Name: {name_of_symbol}")
    print(f"Last Traded Price (LTP): {LTP}")
    print(f"Change in Price (ch): {change_in_price}")
    print(f"Open Price: {open_price}")
    print(f"High Price: {high_price}")
    print(f"Low Price: {low_price}")
    print(f"Previous Close Price: {prev_close_price}")
    print(f"Volume: {volume}")

else:
    print("Could not retrieve data from the response.")


# Live Market Depth
data = {
    "symbol":"MCX:NATURALGAS25AUGFUT",
    "ohlcv_flag":"1"
}

response = fyers.depth(data=data)
#print(response)

if response and response.get('s') == 'ok' and response.get('d'):
    symbol_data = response['d'][list(response['d'].keys())[0]] # Get the data for the first (and likely only) symbol
    atp = symbol_data.get('atp', 'N/A')
    upper_circuit = symbol_data.get('upper_ckt', 'N/A')
    lower_circuit = symbol_data.get('lower_ckt', 'N/A')

    print(f"Average Trading Price (ATP): {atp}")
    print(f"Upper Circuit: {upper_circuit}")
    print(f"Lower Circuit: {lower_circuit}")
else:
    print("Could not retrieve market depth data from the response.")