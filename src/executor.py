from utils import (
    create_engine,
    get_db_url,
    execute_query,
    read_sql_queries,
    select_query
)


index = int(input("Enter sql query index number to execute: "))

queries = read_sql_queries("./sql/base_queries.sql")
query = select_query(queries, index)
engine = create_engine(get_db_url("./secrets/secrets.json"))
result = execute_query(engine, query)


