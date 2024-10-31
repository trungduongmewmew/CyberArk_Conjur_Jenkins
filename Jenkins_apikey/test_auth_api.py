import http.client

# Conjur connection and authentication details
CONJUR_HOST = "conjur-master.poc.local"
CONJUR_ACCOUNT = "POC"
CONJUR_USER_ID = "jenkinstest"
CONJUR_USER_KEY = "3snewv1m1qnt522zdc512rt3yfv1n5cqaj1epbhde3cqt3j5j8pja7"

# Paths for password and username variables
CONJUR_SECRET_PASSWORD_PATH = "vault/LOB_Usersync1/Testing_Conjur/conjur_test_11.200/password"
CONJUR_SECRET_USERNAME_PATH = "vault/LOB_Usersync1/Testing_Conjur/conjur_test_11.200/username"

# Establish HTTPS connection
conn = http.client.HTTPSConnection(CONJUR_HOST)

# Authentication request
auth_request = f"/authn/{CONJUR_ACCOUNT}/{CONJUR_USER_ID}/authenticate"
headers = {
  'Accept-Encoding': 'base64',
  'Content-Type': 'text/plain'
}
conn.request("POST", auth_request, CONJUR_USER_KEY, headers)
res = conn.getresponse()

# Check authentication response
if res.status != 200:
    print("Authentication failed. Status:", res.status, res.reason)
    exit(1)

# Get access token
TOKEN = res.read().decode('ASCII')
print("Access Token:", TOKEN)

# Function to fetch a secret by path
def fetch_secret(secret_path):
    secret_request = f"/secrets/{CONJUR_ACCOUNT}/variable/{secret_path}"
    secret_headers = {
        'Authorization': f"Token token=\"{TOKEN}\""
    }
    conn.request("GET", secret_request, None, secret_headers)
    response = conn.getresponse()
    return response.read().decode("utf-8")

# Fetch password and username
password = fetch_secret(CONJUR_SECRET_PASSWORD_PATH)
username = fetch_secret(CONJUR_SECRET_USERNAME_PATH)

print("Password:", password)
print("Username:", username)
