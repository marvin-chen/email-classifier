from email_classifier.gmail_integration import GmailClient

def test_gmail():
    """Test fetching emails from Gmail API."""
    try:
        client = GmailClient()
        emails = client.fetch_emails(max_results=5)
        if not emails:
            print("No emails fetched.")
            return
        for email in emails:
            print(f"Email ID: {email['id']}, Snippet: {email['snippet']}")
    except Exception as e:
        print(f"Error testing Gmail API: {e}")

if __name__ == "__main__":
    test_gmail()