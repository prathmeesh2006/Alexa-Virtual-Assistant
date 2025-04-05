# Alexa-Virtual-Assistant
A Python-based voice assistant that listens, understands commands, and responds with actions like playing music, telling time, and more.
# Alexa Virtual Assistant

This is a Python-based virtual assistant project inspired by Amazon Alexa. It uses voice commands to perform various tasks like telling the time, opening websites, playing music, and more.

## Features

- Voice recognition using speech_recognition
- Text-to-speech response using pyttsx3
- Perform actions like:
  - Tell current time and date
  - Search on Google or Wikipedia
  - Open websites (YouTube, Google, etc.)
  - Play music from local files
  - Send emails (with setup)
  - and more...

## Technologies Used

- Python 3
- speech_recognition
- pyttsx3
- webbrowser
- datetime
- os

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/prathmeesh2006/Alexa-Virtual-Assistant.git
   cd Alexa-Virtual-Assistant
   
2. Install the required libraries:
  pip install -r requirements.txt

3. Run the assistant:
     python main.py

Notes
Make sure your microphone is working.
For sending emails, configure your email credentials carefully (consider using environment variables for safety).

License
This project is open-source and available under the MIT License
