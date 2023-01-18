#!/bin/bash
# This script downloads covid data and displays it
DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
echo "ON $TODAY, there were $POSITIVE positive COVID cases"

