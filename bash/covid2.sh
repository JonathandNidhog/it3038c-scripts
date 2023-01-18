#!/bin/bash
# This script downloads covid data and displays it

POSITIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].positive')
TODAY=$(date)
ICU=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].inIcuCurrently')
DEATH=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].death')
DEATHIN=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].deathIncrease')
echo "On $TODAY, there were $POSITIVE positive COVID cases,and $ICU people still in ICU, $DEATH already death because covid, the number of death increased $DEATHIN today."
