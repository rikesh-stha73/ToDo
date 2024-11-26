from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the todo_main home.")