# DjangoAPI + AI Python Questions
Some useful Django API for backend development and AI-generated questions for Python&Django study!

## Installation
Clone this repo:
```bash
git clone https://github.com/gobbez/DjangoAPI
```
Install requirements.txt:
```bash
cd API
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
python manage.py runserver
```

# Ollama AI-generated questions!
Use Postman to do a Post request and enable Ollama to generate N questions about Python and Django!

### How to use
1. Create migrations and launch your server (python manage.py runserver)
2. Open Postman and in the Body write a "times": int 
3. (if in local) use this url http://127.0.0.1:8000/addpythonquiz/
4. Now Ollama will create N rows in the PythonQuiz table!
* <b>Play Game</b> *
5. Use Postman (or browser) to send a GET request and start your study-game! This api call will pick a random question from the table
6. In the Postman send a POST request with the body as a Json format with:
{
  "quizmode": "true",
  "username": "YOUR_USERNAME",
  "quest_id": "QUESTION_ID",
  "answer": "YOUR_ANSWER",
}
7. This will enable you to play the game, and get a right or wrong answer (with points)


## GET functions
You can do different GET functions passing the "ask" param, I list them below:
<ul>
<li><b><u>showusers</u></b> = Show all Users table</li>
<li><b><u>showtotquiz</u></b> = Show the total quiz in the PythonQuiz table</li>
<li><b><u>randomquiz</u></b> = Get a random quiz from the PythonQuiz table, even those you have already answered</li>
<li><b><u>newquiz</u></b> = Get a random quiz that you haven't answered yet</li>
<li><b><u>wrongquiz</u></b> = Get a random quiz from those that you have it wrong</li>
</ul>

## POST functions
You can do different POST functions passing the "quizmode" param, I list them below:
<ul>
<li><b><u>true</u></b> = Enable the game. You can answer a question (use one of the above GET functions to see the question!). In this mode the answer will be saved in the right or wrong Users column to enable "newquiz" or "wrongquiz" GET functions.</li>
<li><b><u>not true</u></b> = Make Ollama create N questions in the PythonQuiz table (use "times" param to say how many questions to add!)</li>
</ul>

Enjoy!


