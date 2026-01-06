# FindFast

## Overview
FindFast is a Chrome extension that allows users to ask questions about the webpage they are currently viewing and receive answers based only on that page’s content.

The extension extracts visible text from the page, sends it to the Django backend for processing, and utilizes a language model to generate clear, concise answers grounded in the provided context.

---

## Features
- Ask natural-language questions about the current webpage
- Answers are generated only from page content
- Keyword-based sentence filtering for relevance
- Source sentences are shown for transparency
- Simple and fast Chrome extension interface
- Django REST-style backend with LLM integration

---

## Tech Stack

### Chrome Extension
- JavaScript (Manifest V3)
- HTML and CSS
- Chrome Extensions API

### Backend
- Python
- Django
- Django REST-style API
- OpenAI API
- python-dotenv

---
## Running the Backend Locally

```bash
cd backend
pip install -r requirements.txt
python manage.py runserver
```
---
## Screenshots
<img width="1573" height="891" alt="image" src="https://github.com/user-attachments/assets/5c846714-d094-4f7f-b542-145d1ac03043" />
<img width="400" height="250" alt="image" src="https://github.com/user-attachments/assets/bca01707-d239-4f13-9da6-b0de86555f5f" />





