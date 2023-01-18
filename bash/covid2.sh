#!/bin/bash
# This script downloads covid data and displays it

POSITIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].negative')
HOSP=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].hospitalized')
ICU=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].inIcuCurrently')
DEATH=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].death')
DEATHIN=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].deathIncrease')
echo "On $TODAY, there were$POSITIVE positive,$NEGATIVE negative COVID cases,and$ICUpeople still in ICU,$DEATH already death because covid,and$HOSP still in hospital the number of death increased$DEATHIN today"
