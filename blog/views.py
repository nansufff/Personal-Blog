from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"blog/index.html")

def posts(request):
    return render(request,"blog/all-posts.html")

def post_detail(request):
    pass