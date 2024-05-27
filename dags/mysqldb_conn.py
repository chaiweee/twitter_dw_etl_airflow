import mysql.connector
import auth


class MySQLHandle:
    def __init__(self):
        self.connection = mysql.connector.connect(
            user=auth.creds['WH_USER'],
            password=auth.creds['WH_PASSWORD'],
            host=auth.creds['WH_HOST'],
            database=auth.creds['WH_DBNAME']
        )
        self.cursor = self.connection.cursor()
        print("connected to mysql db")

    def create_table(self, table_name):
        self.cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id VARCHAR(255) PRIMARY KEY,
            tweet TEXT
        )
        """)
        self.connection.commit()


    def insert_tweet(self, tweet_data):
        try:
            sql_query = (
                        "INSERT INTO tweets "
                        "VALUES(%(tweet_key)s, %(target)s, %(ids)s, %(date)s, %(flag)s, %(user)s, %(text)s)"
                        )
            self.cursor.execute(sql_query, tweet_data)
            self.connection.commit()
            print("All tweets inserted successfully")
        except Exception as e:
            print("Error inserting tweets:", e)

    def delete_tweets(self):
        try:
            sql_query = "DELETE FROM tweets"
            self.cursor.execute(sql_query)
            self.connection.commit()
            print("All tweets deleted successfully")
        except Exception as e:
            print("Error deleting tweets:", e)

    def commit(self):
        self.connection.commit()