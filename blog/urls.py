from django.urls import path

from blog.views import blog, post

app_name = "blog"

urlpatterns = [path("", blog, name="index"), path("post/<int:id>/", post, name="post")]
