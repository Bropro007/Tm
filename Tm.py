import time
import requests

# 1SecMail API URL
BASE_URL = "https://www.1secmail.com/api/v1/"

# Function to generate a random email address
def generate_email():
    response = requests.get(f"{BASE_URL}?action=genRandomMailbox&count=1")
    email = response.json()[0]
    return email

# Function to extract username and domain from the email
def extract_email_parts(email):
    username, domain = email.split('@')
    return username, domain

# Function to check for emails in the inbox
def check_inbox(username, domain):
    response = requests.get(f"{BASE_URL}?action=getMessages&login={username}&domain={domain}")
    emails = response.json()
    return emails

# Function to read the content of a specific email by ID
def read_email(username, domain, message_id):
    response = requests.get(f"{BASE_URL}?action=readMessage&login={username}&domain={domain}&id={message_id}")
    email_content = response.json()
    return email_content

# Main program to automate email verification
def auto_verification():
    # Step 1: Generate a temporary email
    email = generate_email()
    print(f"Generated Email: {email}")
    
    # Step 2: Extract email parts
    username, domain = extract_email_parts(email)

    # Step 3: Wait for verification email (polling the inbox)
    print("Waiting for verification email...")
    while True:
        emails = check_inbox(username, domain)
        if emails:
            print(f"Received {len(emails)} email(s).")
            break
        time.sleep(5)  # Poll inbox every 5 seconds

    # Step 4: Read the email content
    latest_email = emails[0]
    email_id = latest_email['id']
    email_content = read_email(username, domain, email_id)
    print(f"Subject: {email_content['subject']}")
    # print(f"From: {email_content['from']}")
    # print(f"Body: {email_content['body']}")

    # Step 5: Extract verification code or link from the email body
    # Modify this based on your email content structure
    # verification_link = email_content['body']  # Example: If the body contains the link
    # print(f"Verification Link: {verification_link}")

# Run the automation
if __name__ == "__main__":
    auto_verification()
