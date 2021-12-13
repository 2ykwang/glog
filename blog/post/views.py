from django.shortcuts import render

# Create your views here.


def post_detail(request, post_slug):
    return render(request, "post/detail.html", {"post_slug": post_slug})
