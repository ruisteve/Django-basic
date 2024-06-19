import requests
from django.http import Http404
from django.shortcuts import render

POSTS_URL = "https://jsonplaceholder.typicode.com/posts"


def get_posts_data():
    data = requests.get(POSTS_URL).json()
    return data


def get_post_data(id: int) -> dict:
    data = requests.get(f"{POSTS_URL}/{id}").json()
    return data


def blog(request):
    return render(
        request, "blog/index.html", {"text": "BLOG", "posts": get_posts_data()}
    )


def post(request, id):
    post_data = get_post_data(id)
    if not post_data:
        raise Http404("Post does not exist")
    return render(
        request, "blog/index.html", {"text": f"POST {id}", "posts": [post_data]}
    )
