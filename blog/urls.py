from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("posts",views.posts,name="posts"),
    path("posts/<slug:slug>",views.post_detail,name="details")#/posts/my-first-post
]
