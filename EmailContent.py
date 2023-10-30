# email.py
from Config import *
def email_generator(excel_file_name):
    from_email = 'ajithkumar@newgendigital.com'
    from_password = EMAIL_PASSWORD
    #to_email='ajithkumaraji9047@gmail.com'
    #cc_email=''
    to_email='rahul.mandal@tvsmotor.com'
    cc_email = 'arun.reddy@newgendigital.com, priyadharshini@newgendigital.com, prasanth@newgendigital.com,  mayank.jain@tvsmotor.com , raviraj@tvsmotor.com '
    subject = '<Re: TVS Ronin Test Ride Cricket Leads>'

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Cc'] = cc_email
    msg['Subject'] = subject

    # Email body
    body = f'''\
        <html>
        <head>
            <style>
                body {{
                    font-family: Verdana, sans-serif;
                    font-size: 14px;
                    color: black;
                }}
                p {{
                    margin: 10px 0;
                }}
            </style>
        </head>
        <body>
            <p>Hi Rahul,</p>
            <p>Refer to the attachment below for details regarding the TVS Ronin Lead count  form wise for the date  {current_date}.</p>
            <p>Please confirm the count from your  end.</p>
            <b style="color: blue;">Thanks & Regards,<br></b>
            <p>Ajithkumar Sekar | Technical support executive<br>
            Newgen Digital Works Pvt. Ltd.<br>
            M: (+91) 8072467327<br>
            W: <a href="http://www.newgen.co">www.newgen.co</a><br>
            A: Chennai - 600041.</p>
        </body>
        </html>
    '''
    msg.attach(MIMEText(body, 'html'))

    # Attach the Excel file
    excel_attachment = open(excel_file_name, 'rb')
    excel_part = MIMEApplication(excel_attachment.read(), Name=EXCEL_NAME)
    excel_attachment.close()
    excel_part['Content-Disposition'] = f'attachment; filename="{EXCEL_NAME}"'
    msg.attach(excel_part)

    try:
        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)

        # Send the email
        recipients = [to_email] + cc_email.split(', ')
        server.sendmail(from_email, recipients, msg.as_string())
        logging.info("Email sent successfully!")
        print("Email sent successfully!")

    except Exception as e:
        logging.error("An error occurred:", str(e))
        print("An error occurred:", str(e))

    finally:
        server.quit()
