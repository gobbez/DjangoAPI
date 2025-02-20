from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Example
import json

class ExampleView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get(self, request, input_id=None):
        if input_id is None:
            # Select all records
            all_records = Example.objects.values()
            return JsonResponse({"Example table results": list(all_records)})
        else:
            # Select one record
            try:
                one_record = Example.objects.get(id=input_id)
                return JsonResponse(
                    {"Example": {"id": one_record.id, "text": one_record.text, "number": one_record.number}})
            except Example.DoesNotExist:
                return JsonResponse({"error": "Record not found"}, status=404)

    @csrf_exempt
    def post(self, request):
        try:
            print("Request Body (raw):", request.body)
            data = json.loads(request.body.decode('utf-8'))
            print(data)
            input_text = data.get("text")
            input_number = data.get("number")

            if not input_text or input_number is None:
                return JsonResponse({"error": "Missing fields"}, status=400)

            Example.objects.create(text=input_text, number=input_number)
            return JsonResponse({"success": "You have added a new row in the Example table!"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": f"Invalid JSON, {request}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Failed to add a new row: {str(e)}"}, status=500)
