from django.shortcuts import render


def home(request):
    return render(
        request,
        "index.html",
        context={"text": "I am at Home!", "title": "This is Home Page!"},
    )
