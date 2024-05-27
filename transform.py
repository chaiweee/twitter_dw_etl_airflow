from airflow.decorators import task
from couchdb_conn import CouchHandle
import re

db_name = "twitter_data_staging"

def text_preprocessing(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+', '', text)  # Remove mentions
    text = re.sub(r'#\w+', '', text)  # Remove hashtags
    text = re.sub(r'[^a-z\s]', '', text)  # Remove non-alphabetical characters
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
    return text


@task(task_id="transform")
def TransformData():
    ch = CouchHandle()
    db = ch.get_database(db_name)
    for id in db:
        doc = db[id]
        if 'text' in doc:
            original_text = doc['text']
            clean_text = text_preprocessing(original_text)
            doc["text"] = clean_text
            ch.insertDoc(db_name, doc)

    print("Data transformation complete and saved back to CouchDB")


