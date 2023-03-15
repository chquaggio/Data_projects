# Read the API key from file
API_KEY=$(cat /home/dev/Data_projects/api_token_sportmonks.txt)

# Define the endpoint and parameters
ENDPOINT="fixtures"
INCLUDE="statistics"
ID=216268
# Construct the URL for the API request
URL_BASE="https://api.sportmonks.com/v3/football"

FILENAME="${ENDPOINT}_${INCLUDE}.json"

# Make the API request and save the response to a file

curl -X GET "${URL_BASE}/${ENDPOINT}/${ID}&include=${INCLUDE}" -H "Authorization: ${API_KEY}" -o "$FILENAME"
