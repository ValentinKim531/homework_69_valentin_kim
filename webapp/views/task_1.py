from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
import json

from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(f'Only GET request are allowed {request.method}')


def add(request, *args, **kwargs):
    if request.method == 'POST' and request.body:
        try:
            fields = json.loads(request.body)
            sum = fields['A'] + fields['B']
            answer_as_json = json.dumps({"answer": sum}, indent=2)
            response = HttpResponse(answer_as_json, content_type='application/json')
        except Exception:
            response_data = {'detail': 'Некорректный набор данных'}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


def subtract(request, *args, **kwargs):
    if request.method == 'POST' and request.body:
        try:
            fields = json.loads(request.body)
            sub = fields['A'] - fields['B']
            answer_as_json = json.dumps({"answer": sub}, indent=2)
            response = HttpResponse(answer_as_json, content_type='application/json')
        except Exception:
            response_data = {'detail': 'Некорректный набор данных'}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


def multiply(request, *args, **kwargs):
    if request.method == 'POST' and request.body:
        try:
            fields = json.loads(request.body)
            mult = fields['A'] * fields['B']
            answer_as_json = json.dumps({"answer": mult}, indent=2)
            response = HttpResponse(answer_as_json, content_type='application/json')
        except Exception:
            response_data = {'detail': 'Некорректный набор данных'}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


def divide(request, *args, **kwargs):
    if request.method == 'POST' and request.body:

        try:
            fields = json.loads(request.body)
            div = fields['A'] / fields['B']
            answer_as_json = json.dumps({"answer": div}, indent=2)
            response = HttpResponse(answer_as_json, content_type='application/json')
        except ZeroDivisionError as e:
            response_data = {"error": "Division by zero!"}
            response = JsonResponse(response_data)
        except Exception:
            response_data = {'detail': 'Некорректный набор данных'}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


