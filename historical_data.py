from fyers_apiv3 import fyersModel
import pandas as pd

with open("fyers_client_id.txt", "r") as f:
    client_id = f.read().strip()

with open("fyers_access_token.txt", "r") as f:
    access_token = f.read().strip()


fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="logs/")

data = {
    "symbol":"MCX:NATURALGAS25AUGFUT",
    "resolution":"240",
    "date_format":1,
    "range_from":"2025-05-12",
    "range_to":"2025-08-08",
    "cont_flag":1,
}

response = fyers.history(data=data)
print(response)

# Saving candles data to csv file

if "candles" in response:
    df = pd.DataFrame(response["candles"], columns=["Epoch", "Open", "High", "Low", "Close", "Volume"])
    df["IST"] = pd.to_datetime(df["Epoch"], unit="s").dt.tz_localize("UTC").dt.tz_convert("Asia/Kolkata")
    df.to_csv("data/NATURALGAS25AUGFUT.csv", index=False)
    print(df)
else:
    print("No candle data found in response.")