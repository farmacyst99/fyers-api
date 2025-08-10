from fyers_apiv3 import fyersModel
import urllib.parse
import os
from dotenv import load_dotenv

# Replace these values with your actual API credentials
# Load environment variables from .env file
load_dotenv()

client_id = os.getenv("FYERS_CLIENT_ID")
secret_key = os.getenv("FYERS_SECRET_KEY")
redirect_uri = os.getenv("FYERS_REDIRECT_URI")
response_type = "code"
state = "sample_state"

# Create a session model with the provided credentials
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type
)


# Generate the auth code using the session model
response = session.generate_authcode()

# Print the auth code received in the response
print(response)

auth_url = input("Enter the auth URL: ")

# Parse the URL to extract the query parameters
parsed_url = urllib.parse.urlparse(auth_url)
query_params = urllib.parse.parse_qs(parsed_url.query)

# Extract the 'auth_code' parameter
auth_code = query_params.get('auth_code', [None])[0]

# Print the extracted auth code to verify
print(f"Extracted Auth Code: {auth_code}")

# Generate the access token using the auth code
grant_type="authorization_code"
auth_code=auth_code

session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type,
    grant_type=grant_type
)

# Set the authorization code in the session object
session.set_token(auth_code)

# Generate the access token using the authorization code
response = session.generate_token()

# Print the response, which should contain the access token and other details
#print(response)

# storing access token in a variable to be used for later
access_token = response.get('access_token')

# Save access token to a file
# Extract the access token from the response
access_token = response.get('access_token')

# Define the filenames
access_token_filename = "fyers_access_token.txt"
client_id_filename = "fyers_client_id.txt"

# Save the access token to a text file
if access_token:
    with open(access_token_filename, "w") as f:
        f.write(access_token)
    print(f"Access token saved to {access_token_filename}")
else:
    print("Access token not found in the response.")

# Save the client ID to a text file
if client_id:
    with open(client_id_filename, "w") as f:
        f.write(client_id)
    print(f"Client ID saved to {client_id_filename}")
else:
    print("Client ID not found.")


# ...existing code...

# Define .env file path and initialize env_vars dictionary
env_path = ".env"
env_vars = {}

# Read existing .env variables if the file exists
if os.path.exists(env_path):
    with open(env_path, "r") as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                env_vars[key] = value

# Update or add access_token and client_id
if access_token:
    env_vars["FYERS_ACCESS_TOKEN"] = access_token
    print(f"Access token updated in {env_path}")
else:
    print("Access token not found in the response.")

if client_id:
    env_vars["FYERS_CLIENT_ID"] = client_id
    print(f"Client ID updated in {env_path}")
else:
    print("Client ID not found.")

# Write back to .env file
with open(env_path, "w") as f:
    for key, value in env_vars.items():
        f.write(f"{key}={value}\n")