from django.shortcuts import render
from django.http import JsonResponse


def app_view(request):
    return render(request, 'index.html')


def teste_api(request):
    return JsonResponse({'teste': None})
