#!/bin/bash

# Leggi la chiave API dal file
API_KEY=$(cat /home/christian/key.txt)

# Effettua la richiesta all'API
curl -X GET \
  "https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2022-02-24" \
  -H "X-RapidAPI-Key: $API_KEY" \
  -H "Accept: application/json"
