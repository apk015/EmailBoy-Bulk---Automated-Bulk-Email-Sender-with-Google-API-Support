# EmailBoy Bulk - Email Sending Tool

EmailBoy Bulk is an advanced bulk email sending tool that supports sending emails via the Google Gmail API. 

## Features
- Send bulk emails to multiple recipients.
- Supports sending personalized emails using templates.
- Automatically handles email sending limits.
- Provides detailed logging of the email sending process.

## Setup

### Prerequisites
- Python 3.6 or higher
- Google account with Gmail API enabled

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/emailboy-bulk.git
    cd emailboy-bulk
    ```

2. Install the required Python packages:
    ```sh
    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client python-dotenv
    ```

3. Set up your environment variables in a `.env` file:
    ```
    # .env file
    YOUR_ENV_VARIABLE=value
    ```

4. Create `config.json` with the following content:
    ```json
    {
        "emails_per_hour": 20,
        "wait_time_seconds": 180
    }
    ```

5. Prepare your email templates:
    - `subject.txt`: Template for email subject.
    - `body.txt`: Template for email body.

6. Prepare your data file:
    - `data.csv`: CSV file containing email addresses and names.

### Usage

1. Run the script:
    ```sh
    python t.py
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
