import pytest
from email_classifier.classifier import EmailClassifier
from unittest.mock import patch, Mock

@pytest.fixture
def classifier():
    return EmailClassifier(ollama_url="http://mock-ollama", model="test-model")

@patch("requests.post")
def test_classify_email_positive(mock_post, classifier):
    mock_response = Mock()
    mock_response.json.return_value = {"response": "This is a positive email."}
    mock_response.raise_for_status.return_value = None
    mock_post.return_value = mock_response
    
    result = classifier.classify_email("Great news! You won a prize!")
    assert result == "positive"

@patch("requests.post")
def test_classify_email_empty(mock_post, classifier):
    result = classifier.classify_email("")
    assert result == "neutral"

@patch("requests.post")
def test_classify_email_error(mock_post, classifier):
    mock_post.side_effect = requests.RequestException("API error")
    result = classifier.classify_email("Test email")
    assert result == "neutral"