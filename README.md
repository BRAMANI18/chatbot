# Student Helpdesk Chatbot

## Overview
The **Student Helpdesk Chatbot** is a rule-based system designed to assist students by providing automated responses to their queries. This chatbot matches user inputs with predefined intents and returns appropriate responses based on a structured dataset. It is a simple yet effective tool for handling common questions in a student helpdesk environment.

## Features
- Automates query resolution for common student inquiries.
- Matches user inputs with intents from a structured dataset.
- Provides fallback responses for unrecognized queries.
- Modular and scalable design for adding new intents and patterns.
- Lightweight and easy to deploy.

## Tech Stack
- **Programming Language**: Python
- **Libraries**: Pandas
- **Dataset**: CSV file containing intents, patterns, and responses

## Installation and Setup
1. Clone the repository to your local machine.
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory.
   ```bash
   cd student-helpdesk-chatbot
   ```
3. Ensure you have Python installed (version 3.7 or higher).
4. Install required dependencies.
   ```bash
   pip install pandas
   ```
5. Place your dataset file (`studenthelpdeskDATASET.csv`) in the project directory.
6. Run the chatbot script.
   ```bash
   python chatbot.py
   ```

## How It Works
1. The chatbot reads a CSV dataset containing `Intent`, `Patterns`, and `Responses` columns.
2. User input is converted to lowercase for consistent matching.
3. The chatbot iterates through the dataset to find an intent matching the input.
4. If a match is found, the corresponding response is returned; otherwise, a fallback message is provided.
5. The chatbot runs in a loop, allowing continuous interaction until the user types "exit".

## Future Enhancements
- Integrate NLP techniques for advanced intent recognition.
- Add support for multilingual responses.
- Develop a web or mobile interface for improved usability.

## Example
```
Chatbot: Hello! How can I assist you today?
You: What are the library timings?
Chatbot: The library is open from 9 AM to 8 PM on weekdays and 10 AM to 5 PM on weekends.
You: exit
Chatbot: Goodbye!
```

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request for any improvements or bug fixes.
