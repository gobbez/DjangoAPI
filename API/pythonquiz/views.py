from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import PythonQuiz
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
        random_question = PythonQuiz.objects.order_by("?").first()
        if not random_question:
            return JsonResponse({"error": "No questions available"}, status=404)

        return JsonResponse(
            {"Quiz": {
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
            times = int(data.get("times"))
            for i in range(times):
                # Add (times) question(s) to the table with Ollama questions
                question = create_question()
                print(question)
                PythonQuiz.objects.create(**question)
            return JsonResponse({"success": f"You have added {times} new row(s) in the PythonQuiz table!"}, status=200)
        except Exception as e:
            return JsonResponse({"error": f"Failed to add a new row: {str(e)}"}, status=500)


