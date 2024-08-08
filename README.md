# EmailBoy Bulk - Advanced Bulk Email Sending Tool

**EmailBoy Bulk** is an advanced and efficient bulk email sending tool designed to streamline the process of sending personalized emails to multiple recipients. Leveraging the Google Gmail API, it ensures reliable and secure email delivery. The tool is perfect for businesses, marketers, and developers who need to send bulk emails with ease.

## Features
- **Bulk Email Sending**: Send emails to multiple recipients with a single script execution.
- **Personalized Emails**: Use templates for email subjects and bodies to personalize messages.
- **Rate Limiting**: Automatically handles Gmail's email sending limits with configurable parameters.
- **Detailed Logging**: Provides real-time logging, including the total emails sent, emails sent per hour, and remaining emails.
- **Error Handling**: Logs failed email attempts for later review and retry.
- **CSV Support**: Reads recipient details from a CSV file, allowing easy management of email lists.

## Setup

### Prerequisites
- Python 3.6 or higher
- Google account with Gmail API enabled

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/emailboy-bulk.git
    cd emailboy-bulk
    ```

2. **Install the required Python packages**:
    ```sh
    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client python-dotenv
    ```

3. **Set up your environment variables in a `.env` file**:
    ```
    # .env file
    YOUR_ENV_VARIABLE=value
    ```

4. **Create `config.json` with the following content**:
    ```json
    {
        "emails_per_hour": 20,
        "wait_time_seconds": 180
    }
    ```

5. **Prepare your email templates**:
    - `subject.txt`: Template for email subject.
    - `body.txt`: Template for email body.

6. **Prepare your data file**:
    - `data.csv`: CSV file containing email addresses and names.

### Usage

1. **Run the script**:
    ```sh
    python t.py
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
