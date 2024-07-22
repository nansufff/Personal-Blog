from django.shortcuts import render,get_object_or_404
from datetime import date
from .models import blogpost
# Create your views here.

def home(request):
    latest_posts=blogpost.objects.all().order_by("-date")[:3]
    return render(request,"blog/index.html",{
        "posts":latest_posts
    })

def posts(request):
    all_posts=blogpost.objects.all()
    return render(request,"blog/all-posts.html",{
        "all_posts":all_posts
    })

def post_detail(request,slug):
    identified_post=get_object_or_404(blogpost,slug=slug)
    return render(request,"blog/post-detail.html",{
        "post":identified_post,
        "tags":identified_post.tags.all()
    })