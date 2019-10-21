import psycopg2
import pandas as pd
import numpy as np
import settings
import os
import shutil

PATH = settings.PATH
PORT = settings.PORT
DBNAME = settings.DBNAME
USER = settings.USER
PSW = settings.PASSWORD
CSVPATH = '../csvfile'

def insert_db(text, cur):
    sql = "insert into tweets(tweet) values('');".format(text)
    cur.execute(sql)
    connection.commit()

if __name__ == '__main__':
    # connection information
    connection_config = 'host={} port={} dbname={} user={} password={}'
    connection_config = connection_config.format(PATH, PORT, DBNAME, USER, PSW)

    # connection
    connection = psycopg2.connect(connection_config)
    cur = connection.cursor()
    
    # read dir
    files = os.listdir(CSVPATH)

    # insert
    for f in files:
        csv_df = pd.read_csv(CSVPATH+'/'+f, engine='python')
        print(f)
        csv_df.apply(lambda row: insert_db(row, cur))

    # test
    cur.execute('select * from tweets limit 5;')
    for c in cur:
        print(c)

    cur.close()
    connection.close()
    
    # delete csv files
    shutil.rmtree(CSVPATH)
    os.mkdir(CSVPATH)
