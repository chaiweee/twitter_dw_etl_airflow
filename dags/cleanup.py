from airflow.decorators import task
from couchdb_conn import CouchHandle

db_name = "twitter_data_staging"

@task(task_id="cleanup")
def CleanUP():
    ch = CouchHandle()
    db = ch.get_database(db_name)
    rows = db.view('_all_docs', include_docs=True)
    docs = []
    for row in rows:
        if row['id'].startswith('_'):
            continue
        doc = row['doc']
        doc['_deleted'] = True
        docs.append(doc)
    db.update(docs)


