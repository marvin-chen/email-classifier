from email_classifier.classifier import EmailClassifier
from email_classifier.gmail_integration import GmailClient

def main():
    # Initialize components
    classifier = EmailClassifier()
    gmail_client = GmailClient()

    # Fetch emails
    emails = gmail_client.fetch_emails(max_results=5)
    if not emails:
        print("No emails fetched.")
        return

    # Classify and label emails
    for email in emails:
        label = classifier.classify_email(email["snippet"])
        print(f"Email {email['id']} classified as: {label}")
        gmail_client.apply_label(email["id"], label)

if __name__ == "__main__":
    main()