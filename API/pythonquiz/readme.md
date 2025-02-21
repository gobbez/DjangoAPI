# Ollama AI-generated questions!
Use Postman to do a Post request and enable Ollama to generate N questions about Python and Django!

### How to use
1. Create migrations and launch your server (python manage.py runserver)
2. Open Postman and in the Body write a "times": int 
3. (if in local) use this url http://127.0.0.1:8000/addpythonquiz/
4. Now Ollama will create N rows in the PythonQuiz table!
5. Use Postman (or browser) to send a GET request and start your study-game! This api call will pick a random question from the table

Enjoy!

PS: Further improvements would be to add another table to save your answers/points or wrong answers..