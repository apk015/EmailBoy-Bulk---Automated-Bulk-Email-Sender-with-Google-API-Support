# 📧 EmailBoy Bulk - Automated Bulk Email Sender with Google API Support 🚀

**EmailBoy Bulk** is an advanced and efficient bulk email sending tool designed to streamline the process of sending personalized emails to multiple recipients. Leveraging the Google Gmail API, it ensures reliable and secure email delivery. This tool is perfect for businesses, marketers, and developers who need to send bulk emails with ease.

## 🌟 Features
- **Bulk Email Sending**: Send emails to multiple recipients with a single script execution.
- **Personalized Emails**: Use templates for email subjects and bodies to personalize messages.
- **Rate Limiting**: Automatically handles Gmail's email sending limits with configurable parameters.
- **Detailed Logging**: Provides real-time logging, including the total emails sent, emails sent per hour, and remaining emails.
- **Error Handling**: Logs failed email attempts for later review and retry.
- **CSV Support**: Reads recipient details from a CSV file, allowing easy management of email lists.

## 🛠️ Setup

### Prerequisites
- Python 3.6 or higher
- Google account with Gmail API enabled

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/apk015/EmailBoy-Bulk---Automated-Bulk-Email-Sender-with-Google-API-Support.git
    cd EmailBoy-Bulk---Automated-Bulk-Email-Sender-with-Google-API-Support
    ```

2. **Install the required Python packages**:
    ```sh
    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client python-dotenv
    ```

3. **Set up your environment variables in a `.env` file**:
    ```dotenv
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
    - **`subject.txt`**: Template for email subject.
      ```txt
      Hello {{name}}, your subject here!
      ```
    - **`body.txt`**: Template for email body.
      ```txt
      Hi {{name}},

      This is the body of your email.

      Best regards,
      Your Company
      ```

6. **Prepare your data file**:
    - **`data.csv`**: CSV file containing email addresses and names.
      ```csv
      email,name
      example1@example.com,John Doe
      example2@example.com,Jane Smith
      ```

### 🔐 Setting Up `credentials.json`

To enable Gmail API, follow these steps:

1. **Go to the Google Cloud Console**:
   [Google Cloud Console](https://console.cloud.google.com/)

2. **Create a new project** or select an existing project.

3. **Enable the Gmail API**:
   - Navigate to "APIs & Services > Library".
   - Search for "Gmail API" and enable it.

4. **Create OAuth 2.0 credentials**:
   - Navigate to "APIs & Services > Credentials".
   - Click on "Create credentials" and select "OAuth 2.0 Client IDs".
   - Configure the consent screen and set the application type to "Desktop app".
   - Download the `credentials.json` file and place it in your project directory.

5. **Run the script for the first time**:
   ```sh
   python main.py
   ```
   This will open a browser window for you to authorize the application. The authorization tokens will be saved to `token.json`.

### 🚀 Usage

1. **Run the script**:
    ```sh
    python main.py
    ```

### 📂 Detailed File Descriptions

#### `main.py`
This is the main script that handles sending emails using the Gmail API. It reads recipient details from `data.csv`, personalizes the email content using `subject.txt` and `body.txt`, and logs the email sending process.

#### `config.json`
Configuration file that sets the email sending limits to comply with Gmail's rate limiting:
```json
{
    "emails_per_hour": 20,
    "wait_time_seconds": 180
}
```

#### `data.csv`
CSV file containing email addresses and names of the recipients:
```csv
email,name
example1@example.com,John Doe
example2@example.com,Jane Smith
```

#### `subject.txt`
Template for the email subject, supporting placeholders like `{{name}}` for personalization:
```txt
Hello {{name}}, your subject here!
```

#### `body.txt`
Template for the email body, supporting placeholders like `{{name}}` for personalization:
```txt
Hi {{name}},

This is the body of your email.

Best regards,
Your Company
```

#### `.gitignore`
Specifies files and directories to be ignored by Git:
```gitignore
# Ignore credentials and token files
credentials.json
token.json

# Ignore log files
log.txt

# Ignore environment variables file
.env
```

#### `README.md`
This file, providing an overview of the project, setup instructions, and usage details.

#### `LICENSE`
License file specifying the terms under which the project can be used and distributed.

### 📋 Example

Here's a complete example of how your project directory should look:

```
EmailBoy-Bulk---Automated-Bulk-Email-Sender-with-Google-API-Support/
│
├── config.json
├── credentials.json
├── data.csv
├── subject.txt
├── body.txt
├── main.py
├── .gitignore
└── README.md
```

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


