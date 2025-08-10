from fyers_apiv3 import fyersModel
import urllib.parse

# Replace these values with your actual API credentials
client_id = "C46K5Q6PQ0-100"
secret_key = "PIG111ZFOD"
redirect_uri = "https://127.0.0.1:8080"
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
"grant_type"="authorization_code"
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

