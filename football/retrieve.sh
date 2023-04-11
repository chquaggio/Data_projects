#!/bin/bash

# Read the API key from file
API_KEY=$(cat key.txt)

# Define the endpoint and parameters
ENDPOINT="teams"
LEAGUE=135 # Serie A
SEASON=2021 # Change this to the season you want to query

# Construct the URL for the API request
URL="https://v3.football.api-sports.io/$ENDPOINT?league=$LEAGUE&season=$SEASON"
FILENAME="${ENDPOINT}_league${LEAGUE}_season${SEASON}.json"

# Make the API request and save the response to a file
curl -X GET "$URL" -H "x-apisports-key: $API_KEY" -o "$FILENAME"
