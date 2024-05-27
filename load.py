from airflow.decorators import task
from couchdb_conn import CouchHandle
from mysqldb_conn import MySQLHandle
from couchdb_conn import CouchHandle
from datetime import datetime,timezone
import uuid


db_name = "twitter_data_staging"


@task(task_id="load")
def LoadToDW():
    ch = CouchHandle()
    wh = MySQLHandle()

    db = ch.get_database(db_name)
    for id in db:
        doc = db[id]
        try:    
            tweet_key = uuid.uuid4().int & (1<<64)-1

            tweet_data = {
                    'tweet_key': tweet_key,
                    'target': doc.get('target'),
                    'ids': doc.get('ids'),
                    'date': doc.get('date'),
                    'flag': doc.get('flag'),
                    'user': doc.get('user'),
                    'text': doc.get('text')
                } 
            wh.delete_tweets()

            wh.insert_tweet(tweet_data)

        except BaseException as e:
            print("ERROR: ", e)
