#!/usr/bin/env python
# coding: utf-8

#Import libraries
import pandas as pd
import sqlalchemy
import argparse
from sqlalchemy import create_engine
import os



def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url=params.url
    csv_name = "output.csv"

    # Download data
    os.system(f'curl -o {csv_name} {url}')
    
    #Read NY taxi data (yellow taxi, 2021)
    df = pd.read_parquet(csv_name)
    
    # Create engine to load into
    engine = create_engine(f'postgresql://{user}:{password}@localhost:{port}/{db}')

    #print(pd.io.sql.get_schema(df, "yellow_taxi_data", con=engine))
    df.to_sql(name=table_name, con=engine, if_exists="replace", chunksize=100000)


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Ingest CSV Data to Postgres")

    parser.add_argument("--user", help="user name for postgres")
    parser.add_argument("--password", help="pass word for postgres")
    parser.add_argument("--host", help="host for postgres")
    parser.add_argument("--port", help="port for postgres")
    parser.add_argument("--db", help="database name for postgres")
    parser.add_argument("--table_name", help="name of table where we are writing the results to")
    parser.add_argument("--url", help="url of the csv file")

    args = parser.parse_args()

    main(args)