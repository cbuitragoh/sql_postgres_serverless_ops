from sqlalchemy import create_engine, text
import json
import pandas as pd
import re


# create engine
def get_engine(db_url):
    engine = create_engine(db_url)
    return engine


# get url connector
def get_db_url(filepath: str):
    with open(filepath, 'r') as f:
        data = json.load(f)
        db_url = f'postgresql+psycopg2://{data["user"]}:{data["password"]}@{data["host"]}:{data["port"]}/{data["database"]}'

        return db_url


# execute query
def execute_query(engine, query):
    with engine.connect() as conn:
        conn.execution_options(isolation_level="AUTOCOMMIT")
        result = conn.execute(text(query))
        return result


# read csv files
def read_csv(filepath: str):
    df = pd.read_csv(filepath)
    return df


# Overwrite secrets file
def overwrite_secrets(
        filepath: str,
        database: str,
        user: str,
        password: str,
        host: str,
        port: str
):
    """
    this function overwrite secrets file
    with new values

    params 
    -------
    filepath: path to secrets file
    database: database name
    user: user name
    password: password
    host: host name
    port: port number
    """
    with open(filepath, 'r') as f:
        data = json.load(f)
        data['database'] = database
        data['user'] = user
        data['password'] = password
        data['host'] = host
        data['port'] = port
        with open(filepath, 'w') as f:
            json.dump(data, f)
    return True


# read sql queries
def read_sql_queries(filepath: str):
    """
    this function read sql queries from
    base_queries.sql file

    params 
    -------
    filepath: path to base_queries.sql file

    return
    ------- 
    queries: list of queries
    """
    with open(filepath, 'r') as f:
        queries = f.read()
        queries = queries.split(";")
        return queries
    

# select specific query to use
def select_query(queries: list, index:int):
    """
    this function select specific query from
    queries in base_queries.sql file

    params 
    -------
    queries: list of queries
    position: position of query in queries list
    
    return
    ------- 
    query: string
    """
    base_query = queries[index]
    if "{}" in base_query:
        values = []
        input_keys = [x for x in base_query.split('{}')]
        for key in input_keys[:-1]:
            word = key.split(' ')[-2]
            val = input(f"Enter {word}: ")
            values.append(f"'{val}'")
        query = base_query.format(*values)
        return query
    else:
        query = base_query
        return query
        
