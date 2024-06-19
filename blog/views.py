import requests
from django.shortcuts import render


def get_posts_data():
    data = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    return data


def blog(request):
    return render(request, "blog/index.html", {"posts": get_posts_data()})
