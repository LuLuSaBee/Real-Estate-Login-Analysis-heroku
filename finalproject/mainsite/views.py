from django.shortcuts import render
from django.http import JsonResponse


def homepage(request):
    return JsonResponse({'now': 123})
