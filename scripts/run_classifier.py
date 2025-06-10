# This script serves as a simple command-line interface to fetch, clean, and classify emails.

from email_classifier.gmail_integration import fetch_emails
from email_classifier.utils import clean_email_text
from email_classifier.classifier import classify_email

def main():
    emails = fetch_emails()
    for email in emails:
        cleaned_body = clean_email_text(email["body"])
        category = classify_email(cleaned_body)
        print(f"Subject: {email['subject']}")
        print(f"Category: {category}")
        print("-" * 40)

if __name__ == "__main__":
    main()
