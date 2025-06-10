# Email Classifier

A local email classification tool using [Ollama](https://ollama.com/) (local LLM) and the Gmail API. This project aims to automatically categorize emails and apply labels for better inbox management.

---

## Features

- Uses a local LLM via Ollama for classification
- Integrates with Gmail API to fetch and label emails
- Modular design for easy extension and testing

---

## Project Structure

<pre>
email-classifier/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
│
├── email_classifier/
│   ├── __init__.py
│   ├── classifier.py          # Core classification logic using Ollama
│   ├── gmail_integration.py   # Gmail API integration for reading/applying labels
│   └── utils.py               # Helper functions
│
├── tests/
│   └── test_classifier.py     # Unit tests for classifier module
│
└── scripts/
    └── run_classifier.py      # Script to execute the classifier
</pre>

---

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/email-classifier.git
    cd email-classifier
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Additional setup (coming soon):**
    - Configure Gmail API credentials
    - Set up Ollama locally with the desired model

---

## Requirements

- Python 3.10+
- Gmail API credentials
- Ollama installed and running locally
- See `requirements.txt` for full dependency list

---

## License

This project is licensed under the [MIT License](LICENSE).

---

**Note:**  
*This project is a work in progress. Contributions and suggestions are welcome!*
