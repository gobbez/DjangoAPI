# DjangoAPI + AI Python Questions
Some useful Django API for backend development and AI-generated question for Python&Django study!

### Updates
21/02 = Added Ollama LLM chatbot to dynamically generate Python questions in the table
20/02 = Added an Example table with OOP for CRUD

## Installation
Clone this repo:
```bash
git clone https://github.com/gobbez/DjangoAPI
```
Install requirements.txt:
```bash
pip install requirements.txt
```
(optional, if you want to use Ollama to create questions)
```Ollama bash
ollama run gemma2
```
Create migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
Launch Django server:
```bash
cd API
python manage.py runserver
```

## How to use
You can send GET or POST requests via Postman (or browser for get).
Check each folder readme.md to see what you can do, what routes and how you can use them!




