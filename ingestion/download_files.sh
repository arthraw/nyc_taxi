#!/bin/bash

mkdir -p /tmp/raw/yellow_trip
mkdir -p /tmp/lookup

for month in $(seq -w 01 03); do
    echo "Downloading month: ${month}..."
    curl -o /tmp/raw/yellow_trip/yellow_tripdata_2025-${month}.parquet \
        -L "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-${month}.parquet"
done

echo "Downloading taxi zone lookup."
curl -o /tmp/lookup/taxi_zone_lookup.csv \
  -L "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"

echo "All files downloaded successfully."
exit 0