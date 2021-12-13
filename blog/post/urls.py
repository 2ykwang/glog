from django.urls import path

from blog.post import views

app_name = "post"

urlpatterns = [path("<str:post_slug>", views.post_detail, name="post_detail")]
