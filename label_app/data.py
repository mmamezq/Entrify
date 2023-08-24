import pandas as pd
from model import db, connect_to_db
from server import app

pd.set_option('display.max_colwidth', None)
df = pd.read_json('data_081723.json', orient='index', convert_axes=False)

df.index = pd.to_numeric(df.index)

conn = connect_to_db(app, 'li-job-data', echo = True)

df.to_sql('jobs', con = conn, if_exists='append', index = False, chunksize=900)