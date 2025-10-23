from django.shortcuts import render
from django.http import JsonResponse
from .models import Todo

def todo_list(request):
    todos = list(Todo.objects.values())
    return JsonResponse(todos,safe=False)
