from airflow.decorators import task
from couchdb_conn import CouchHandle
import csv

@task(task_id="extract")
def LoadToStaging():
    ch = CouchHandle()

    source_file = "/home/sunnytan/data_source/tweets.csv"
    dest_file = "/home/sunnytan/data_source/tweets_with_header.csv"

    test_file = "/home/sunnytan/data_source/tweets_with_header(test).csv"
    
    db_name = "twitter_data_staging"


    # headerList = ['target', 'ids', 'date', 'flag', 'user', 'text']
    # # Read the original CSV file contents
    # with open(source_file, 'r', newline='', encoding = "ISO-8859-1") as infile:
    #     reader = csv.reader(infile)
    #     rows = [row for row in reader]

    # # Write the new CSV file with the header
    # with open(dest_file, 'w', newline='', encoding = "ISO-8859-1") as outfile:
    #     writer = csv.writer(outfile)
    #     # Write the header first
    #     writer.writerow(headerList)
    #     # Write the original rows
    #     writer.writerows(rows)

    # print(f"Header added and saved to {dest_file}")

    try:

        # Open the CSV file and parse its contents
        with open(test_file, 'r', newline='', encoding = "ISO-8859-1") as file:
            reader = csv.DictReader(file)
            csv_data = [row for row in reader]

        # Convert CSV rows to JSON documents and store in CouchDB

        if ch.check_database_exists(db_name):
            ch.deleteDB(db_name)

        ch.createDB(db_name)

        for row in csv_data:
            json_document = {
                'target': row['target'],
                'ids': row['ids'],
                'date': row['date'],
                'flag': row['flag'],
                'user': row['user'],
                'text': row['text']
                # Add more fields as needed
            }

            ch.insertDoc(db_name, json_document)

    except Exception as e:
        print("ERRORS: ", e)