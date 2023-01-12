from django.shortcuts import render, redirect
from server.apps.posts.models import Post

# Create your views here.
def hello_world(request, *args, **kwargs):
    return render(request, "posts/hello_world.html")

def posts_list(request, *args, **kwargs):
    posts = Post.objects.all()
    return render(request, "posts/posts_list.html",{"posts":posts})

def posts_retrieve(request, pk, *args, **kwargs):
    post=Post.objects.all().get(id=pk)
    return render(request, "posts/posts_retrieve.html", {"post":post})


def posts_create(request, *args, **kwargs):
    if request.method == "POST":
        Post.objects.create(
            title=request.POST["title"],
            user=request.POST["user"],
            region=request.POST["region"],
            price=request.POST["price"],
            content=request.POST["content"],
        )
        # go to home
        return redirect("/")
    return render(request, "posts/posts_create.html")

def posts_delete(request, pk, *args, **kwargs):
    return redirect("/")