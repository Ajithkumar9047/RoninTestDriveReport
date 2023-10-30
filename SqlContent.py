from Config import *

def establish_database_connection():
    server = 'icubemobappsqlprod.database.windows.net'
    database = 'tvs-iqube-dealer-db'
    username = 'ngd'
    password = 'iCube@$1iGvs!n'
    driver = '{ODBC Driver 17 for SQL Server}'
    conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        print("Failed to establish a database connection:", str(e))
        return None, None

def execute_sql_query(cursor):
    try:
        cursor.execute(sql_query)
        return cursor.fetchall()
    except Exception as e:
        print("An error occurred while executing the SQL query:", str(e))
        return []