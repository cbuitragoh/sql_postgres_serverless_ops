"""
With this module we loading example
data to database for apply sql queries
"""

import pandas as pd
import sys
sys.path.append('./src/')
from utils import (create_engine,
                   get_db_url,
                   read_csv)

engine = create_engine(get_db_url('./secrets/secrets.json'))

df = read_csv('./data/creditcard.csv')

with engine.connect() as conn:
    df.to_sql('creditcard', con=conn, if_exists='replace')
    conn.commit()

