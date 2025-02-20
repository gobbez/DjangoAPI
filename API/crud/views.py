from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Example
import json

class ExampleView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        """Use csrf_exampt to enable post methods from other sources"""
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        """This method is used to select all or one row(s)"""
        data = json.loads(request.body.decode('utf-8'))
        input_id = data.get('input_id')

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
        """This method (requires csrf_exempt to enable different origins of calls) is used to
        add a new row in the table (Postman is fine)"""
        try:
            data = json.loads(request.body.decode('utf-8'))
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

    @csrf_exempt
    def put(self, request):
        """This method is called to update a row"""
        try:
            data = json.loads(request.body.decode('utf-8'))
            input_id = data.get("input_id")
            input_text = data.get("text")
            input_number = data.get("number")
            one_record = Example.objects.get(id=input_id)

            if input_text == None and input_number == None:
                return JsonResponse({"error": f"Invalid JSON, {request}"}, status=400)
            if input_text:
                one_record.text = input_text
                one_record.save()
            if input_number:
                one_record.number = input_number
                one_record.save()
            return JsonResponse({"success": "You have updated a row in the Example table!"}, status=200)
        except Exception as e:
            return JsonResponse({"error": f"Failed to update a row: {str(e)}"}, status=500)

    @csrf_exempt
    def delete(self, request):
        """This method is used to delete a row in the table"""
        try:
            data = json.loads(request.body.decode('utf-8'))
            input_id = data.get("input_id")
            one_record = Example.objects.get(id=input_id)
            one_record.delete()
            return JsonResponse({"success": "You have deleted a row in the Example table!"}, status=200)
        except Exception as e:
            return JsonResponse({"error": f"Failed to delete a row: {str(e)}"}, status=500)