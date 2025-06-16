from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email_classifier.utils import clean_email_text

class GmailClient:
    def __init__(self, credentials_path: str = "credentials.json", token_path: str = "token.json"):
        """
        Initialize Gmail API client.
        
        Args:
            credentials_path (str): Path to Gmail API credentials JSON.
            token_path (str): Path to store OAuth token.
        """
        self.scopes = ["https://www.googleapis.com/auth/gmail.modify"]
        self.credentials_path = credentials_path
        self.token_path = token_path
        self.service = self._get_service()

    def _get_service(self):
        """
        Authenticate and build Gmail API service.
        
        Returns:
            Resource: Gmail API service object.
        """
        creds = None
        try:
            creds = Credentials.from_authorized_user_file(self.token_path, self.scopes)
        except FileNotFoundError:
            flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, self.scopes)
            creds = flow.run_local_server(port=0)
            with open(self.token_path, "w") as token:
                token.write(creds.to_json())
        
        return build("gmail", "v1", credentials=creds)

    def fetch_emails(self, max_results: int = 10) -> list:
        """
        Fetch recent emails from the inbox.
        
        Args:
            max_results (int): Maximum number of emails to fetch.
        
        Returns:
            list: List of email dictionaries with id and snippet.
        """
        try:
            results = self.service.users().messages().list(userId="me", maxResults=max_results).execute()
            messages = results.get("messages", [])
            emails = []
            for message in messages:
                msg = self.service.users().messages().get(userId="me", id=message["id"]).execute()
                snippet = msg.get("snippet", "")
                emails.append({"id": message["id"], "snippet": clean_email_text(snippet)})
            return emails
        except Exception as e:
            print(f"Error fetching emails: {e}")
            return []

    def apply_label(self, email_id: str, label: str):
        """
        Apply a label to an email.
        
        Args:
            email_id (str): ID of the email.
            label (str): Label to apply (e.g., 'POSITIVE', 'NEGATIVE', 'NEUTRAL').
        """
        try:
            # Check if label exists, create if not
            labels = self.service.users().labels().list(userId="me").execute().get("labels", [])
            label_id = None
            for lbl in labels:
                if lbl["name"].upper() == label.upper():
                    label_id = lbl["id"]
                    break
            if not label_id:
                label_data = {
                    "name": label.upper(),
                    "labelListVisibility": "labelShow",
                    "messageListVisibility": "show"
                }
                new_label = self.service.users().labels().create(userId="me", body=label_data).execute()
                label_id = new_label["id"]
            
            # Apply label to email
            self.service.users().messages().modify(
                userId="me",
                id=email_id,
                body={"addLabelIds": [label_id]}
            ).execute()
        except Exception as e:
            print(f"Error applying label {label} to email {email_id}: {e}")