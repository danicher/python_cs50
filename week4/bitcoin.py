import requests
import sys

api_key = "579e58faaf49ba95acc2848214444530a0fcd95a9ee5680be0df0eaeee01e730"

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=579e58faaf49ba95acc2848214444530a0fcd95a9ee5680be0df0eaeee01e730")
    price = float(response.json()["data"]["priceUsd"])

    total = n * price
    print(f"${total:,.4f}")

except requests.RequestException:
    sys.exit("Error fetching Bitcoin price")