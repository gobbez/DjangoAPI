from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import PythonQuiz
from .models import Users
import json
import random
from .ollamaquestions import create_question


class PythonQuizView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        """Use csrf_exampt to enable post methods from other sources"""
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        """Get a random question"""
        data = json.loads(request.body.decode('utf-8'))
        ask = data.get("ask")

        if ask == "showusers":
            # Show the user table
            all_users = Users.objects.values()
            return JsonResponse({"Users": list(all_users)})

        elif ask == "showtotquiz":
            # Show the number of questions in the PythonQuiz table
            all_records = PythonQuiz.objects.values()
            return JsonResponse({"Number of questions": len(list(all_records))})

        elif ask == "randomquiz":
            # Get a random question
            random_question = PythonQuiz.objects.order_by("?").first()
            if not random_question:
                return JsonResponse({"error": "No questions available"}, status=404)

            return JsonResponse(
                {"Quiz": {
                    "id": random_question.id,
                    "question": random_question.question,
                    "A": random_question.A,
                    "B": random_question.B,
                    "C": random_question.C,
                    "D": random_question.D,
                    # "correct": random_question.correct,
                    "points": random_question.points
                }}
            )

        elif ask == "newquiz":
            # Filter only questions that you haven't answered yet
            username = data.get("username")
            positive_answers = Users.objects.filter(username=username).exclude(right=0).values_list("right", flat=True)
            negative_answers = Users.objects.filter(username=username).exclude(wrong=0).values_list("wrong", flat=True)
            answered_quiz_ids = set(positive_answers) | set(negative_answers)
            unanswered_quizzes = PythonQuiz.objects.exclude(id__in=answered_quiz_ids)
            # Get a random question
            random_question = unanswered_quizzes.order_by("?").first()
            if not random_question:
                return JsonResponse({"error": "No questions available"}, status=404)

            return JsonResponse(
                {"Quiz": {
                    "id": random_question.id,
                    "question": random_question.question,
                    "A": random_question.A,
                    "B": random_question.B,
                    "C": random_question.C,
                    "D": random_question.D,
                    # "correct": random_question.correct,
                    "points": random_question.points
                }}
            )

        elif ask == "wrongquiz":
            # Filter only questions that you have wrong
            username = data.get("username")
            negative_answers_ids = Users.objects.filter(username=username).exclude(wrong=0).values_list("wrong", flat=True)
            negative_filter = PythonQuiz.objects.filter(id__in=negative_answers_ids)
            # Get a random question
            random_question = negative_filter.order_by("?").first()
            if not random_question:
                return JsonResponse({"error": "No questions available"}, status=404)

            return JsonResponse(
                {"Quiz": {
                    "id": random_question.id,
                    "question": random_question.question,
                    "A": random_question.A,
                    "B": random_question.B,
                    "C": random_question.C,
                    "D": random_question.D,
                    # "correct": random_question.correct,
                    "points": random_question.points
                }}
            )

    @csrf_exempt
    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            quizmode = data.get("quizmode")
            if quizmode == "true":
                # Play! It requires the id of the question and your answer (letter)
                username = data.get("username")
                quest_id = data.get("quest_id")
                answer = data.get("answer")
                correct_answer = PythonQuiz.objects.get(id=quest_id)
                solution = correct_answer.correct
                points = correct_answer.points

                # Check if your answer is correct
                if answer == solution:
                    record = Users.objects.get(wrong=quest_id)
                    if record:
                        # Delete the row of the wrong answer in the Users table
                        record.delete()
                    # Save the question id in the right column of Users
                    Users.objects.create(username=username, right=quest_id, wrong=0)
                    return JsonResponse({"success": f"Great job! You won: {points} points!"}, status=200)
                else:
                    record = Users.objects.get(right=quest_id)
                    if record:
                        # Delete the row of the right answer in the Users table
                        record.delete()
                    # Save the question id in the wrong column of Users
                    Users.objects.create(username=username, wrong=quest_id, right=0)
                    return JsonResponse({"failed": f"Wrong! Try again!"}, status=200)

            else:
                # Let AI create questions in the table
                times = int(data.get("times"))
                for i in range(times):
                    # Add (times) question(s) to the table with Ollama questions
                    question = create_question()
                    print(question)
                    PythonQuiz.objects.create(**question)
                return JsonResponse({"success": f"You have added {times} new row(s) in the PythonQuiz table!"}, status=200)
        except Exception as e:
            return JsonResponse({"error": f"Failed to add a new row: {str(e)}"}, status=500)


