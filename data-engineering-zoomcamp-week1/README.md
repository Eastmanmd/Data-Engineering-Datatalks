# Week 1: Docker, Postgres, Terraform, and GCP
## Overview
This project focuses on setting up a Dockerized PostgreSQL database for NYC taxi data, building a data pipeline, conducting query analysis, and deploying infrastructure with Terraform. The README includes detailed instructions and queries for each task.

## Docker Setup
### PostgreSQL Container
Command to start a PostgreSQL Docker container:
```bash
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v d://data-engineering-zoomcamp//week_1//2_docker_sql//ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network=pg-network \
    --name pg-database \
    postgres:16.6
```
### pgAdmin Container
Command to launch a Docker Container containing pgAdmin running in server mode:
```bash
docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network
    --name pgadmin
    dpage/pgadmin4
```

## Data Pipeline
### Building Docker Image
Build a Docker image for the data ingestion pipeline:
```bash
docker build -t taxi_data_ingestion:v001 .
```

### Running Data Pipeline Container
Ingestion pipeline container:
```bash
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz"

docker run -it ingest_data.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table_name=green_taxi_trips \
    --url=${URL}
```

