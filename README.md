# Twitter ETL Data Warehouse Project

This project builds an ETL pipeline that sources data from Twitter, applies transformations, and stores it in a MySQL Data Warehouse. The project leverages Apache Airflow for workflow management, CouchDB for intermediary storage, and MySQL for the data warehouse.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Airflow DAG](#airflow-dag)


## Technologies Used
- Python
- Apache Airflow
- MySQL
- Docker
  
## Installation

### Prerequisites
- WSL
- Python 3.7+
- Docker
- MySQL
- Apache Airflow

### Steps

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/twitter-etl.git
   cd twitter-etl
   
2. Set up the Python environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt

3. Setup CouchDB using Docker
   ```sh
   docker run -d --name couchdb -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=password -p 5984:5984 couchdb

4. Install MYSQL

5. Setup Airflow
   ```sh
   export AIRFLOW_HOME=$(pwd)/airflow
   airflow db init
   airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com

6. Airflow.cfg configure
   ```sh
   [core]
   ...
   dags_folder = /path/to/your/dags

   
## Usage
1. Start Airflow Webserver and Scheduler
   ```sh
   airflow scheduler &
   airflow webserver --port 8080 &

2. Access the Airflow UI:
Open a web browser and go to http://localhost:8080. Log in with the credentials you created (admin/admin).

3. Trigger the DAG:
In the Airflow UI, locate the twitter_wh_dag and trigger it manually or wait for the scheduled run.

## Airflow DAG

### DAG Structure
Extract Task: Reads tweet data from a CSV file and stores it in CouchDB.  
Transform Task: Cleans and processes tweet text data.  
Load Task: Loads the transformed data into the MySQL data warehouse.  
Cleanup Task: Cleans up intermediary data and logs.  



