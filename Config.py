# config.py
import pyodbc
from datetime import datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Border, Side
import os
import logging

# Configure the logging
logging.basicConfig(
    filename='project.log',  # Name of the log file
    level=logging.DEBUG,     # Minimum log level to record (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s [%(levelname)s]: %(message)s',
)

#from decouple import Config, Csv

#config = Config()
#config.read('.env')

#EMAIL_PASSWORD = config('testPW', default='', cast=str)
EMAIL_PASSWORD ='uroqpjoiixmnrxxb'

current_date = datetime.now().strftime('%d/%m/%Y')
#yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%d/%m/%Y')
yesterday_date='01/10/2023'
EXCEL_NAME=f"TRC Area wise Update_{current_date}.xlsx"
path="D:/tvsexcel"

sql_query = """
select mst.Dealer_ID,mst.Dealer_Name,
mst.Zone,mst.Area,mst.State,mst.City,mst.Teri,mst.Indus_town,
COUNT(form.id) as total
from
Ronin_dealer_master mst left join Ronin_test_ride_form form
on mst.Dealer_ID=form.Dealer_Code
group by mst.Dealer_ID,mst.Dealer_Name,mst.Zone,mst.Area,mst.State,
mst.City,mst.Teri,mst.Indus_town
order by COUNT(form.id) desc
"""
