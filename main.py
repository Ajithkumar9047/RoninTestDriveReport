from Config import *
from SqlContent import establish_database_connection, execute_sql_query
from EmailContent import email_generator
from ExcelContent import create_excel
from datetime import datetime, timedelta

current_date = datetime.now().strftime('%d/%m/%Y')
yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%d/%m/%Y')

def main():
    conn, cursor = establish_database_connection()

    if conn and cursor:
        rows_query1 = execute_sql_query(cursor)
        print(rows_query1)
        excel_file_name = create_excel(rows_query1)
        email_generator(excel_file_name)
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
