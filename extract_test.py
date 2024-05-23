from airflow.decorators import task
# from extract import DataHandle
from couchdb_conn import CouchHandle
# from datetime import datetime,timezone,timedelta
import pandas as pd

@task(task_id="extract")
def LoadToStaging():
    ch = CouchHandle()

    df = pd.read_csv("/home/sunnytan/data_source/tweets.csv", encoding = "ISO-8859-1")

    print(df.describe())

    try:
        ch.insert({
                    "tweet": tweet,
                    "user": users[idx]
                })
    except BaseException as e:
        print("ERRORS: ", e)



df = pd.read_csv("/home/sunnytan/data_source/tweets.csv", encoding = "ISO-8859-1")

df.describe()

df.columns = ['target', 'ids', 'date', 'flag', 'user', 'text']

print(list(df.columns))