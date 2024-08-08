import os
import csv
import time
import json
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv
from email.utils import formataddr

# Load environment variables
load_dotenv()

# Configuration settings
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

EMAILS_PER_HOUR = config.get('emails_per_hour', 20)
WAIT_TIME_SECONDS = config.get('wait_time_seconds', 180)

# Scopes for Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Get credentials and create an API client
def get_credentials():
    creds = None
    # Path to the credentials.json file you downloaded
    credentials_file = 'credentials.json'
    # Token file stores the user's access and refresh tokens
    token_file = 'token.json'
    
    # Load credentials from token file, if it exists
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    # If there are no valid credentials available, request authorization
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                creds = None
                print(f"Error refreshing credentials: {e}")
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file, 'w') as token:
            token.write(creds.to_json())
    return creds

# Function to send email
def send_email(creds, recipient_name, recipient_email):
    # Read subject and body templates
    with open('subject.txt', 'r') as file:
        subject_template = file.read()
    with open('body.txt', 'r') as file:
        body_template = file.read()

    # Replace placeholders with actual data
    subject = subject_template.replace('{{name}}', recipient_name)
    body = body_template.replace('{{name}}', recipient_name)

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = formataddr(('FlySpark', 'info@flyspark.in'))  # Use the custom email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    # Encode message in base64
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    message = {'raw': raw}

    # Build the Gmail API service
    service = build('gmail', 'v1', credentials=creds)
    
    # Send the email
    try:
        message = (service.users().messages().send(userId="me", body=message).execute())
        log_message(f"Email sent successfully to {recipient_email}")
        return True
    except Exception as e:
        log_message(f"Failed to send email to {recipient_email}: {str(e)}")
        return False

# Helper function to log messages
def log_message(message, filename='log.txt'):
    with open(filename, 'a') as log_file:
        log_file.write(message + '\n')
    print(message)

# Function to process emails from the CSV
def process_emails():
    # Keep track of sent emails
    total_sent_emails = 0
    sent_emails_count = 0
    failed_emails = []

    # Get credentials
    creds = get_credentials()

    while True:
        if not os.path.exists('data.csv'):
            log_message("No data.csv file found.")
            break

        with open('data.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            rows = list(csv_reader)

            if not rows:
                log_message("No more emails to send. Process complete.")
                break

            # Process each row
            row_processed = False
            for row in rows:
                if 'email' in row and 'name' in row:
                    recipient_emails = row['email'].split(',')  # Split multiple emails
                    recipient_name = row['name']

                    for recipient_email in recipient_emails:
                        recipient_email = recipient_email.strip()  # Remove any extra spaces

                        # Send the email
                        if send_email(creds, recipient_name, recipient_email):
                            sent_emails_count += 1
                            total_sent_emails += 1
                            row_processed = True
                            remaining_emails = len(rows) - 1
                            log_message(f"Email sent to: {recipient_email}")
                            log_message(f"Total emails sent: {total_sent_emails}")
                            log_message(f"Emails sent this hour: {sent_emails_count}")
                            log_message(f"Remaining emails: {remaining_emails}")
                        else:
                            failed_emails.append({'email': recipient_email, 'name': recipient_name})

                        # Check the email limit
                        if sent_emails_count >= EMAILS_PER_HOUR:
                            log_message(f"Reached email limit of {EMAILS_PER_HOUR} emails. Waiting for {WAIT_TIME_SECONDS} seconds...")
                            time.sleep(WAIT_TIME_SECONDS)
                            sent_emails_count = 0

                    if row_processed:
                        break  # Exit the loop to process the next row

            # Remove the processed row from the CSV file
            if row_processed:
                rows.remove(row)
                with open('data.csv', 'w', newline='', encoding='utf-8') as csv_file:
                    fieldnames = ['email', 'name']
                    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    csv_writer.writerows(rows)

    if failed_emails:
        log_message(f"Failed emails: {failed_emails}")

    log_message(f"Total emails sent: {total_sent_emails}")

if __name__ == '__main__':
    process_emails()
