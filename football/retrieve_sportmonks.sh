# Read the API key from file
export $(grep -v '^#' .env | xargs)

# Define the endpoint and parameters
ENDPOINT="fixtures"
INCLUDE="statistics"
ID=216268
# Construct the URL for the API request
URL_BASE="https://api.sportmonks.com/v3/football"

COMPLETE_URL="${URL_BASE}/${ENDPOINT}/${ID}?api_token=${API_KEY}&include=${INCLUDE}"
FILENAME="${ENDPOINT}_${INCLUDE}.json"
echo $COMPLETE_URL

# Make the API request and save the response to a file

curl -X GET $COMPLETE_URL -o $FILENAME
