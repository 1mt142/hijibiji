from django.urls import path
from .views import CreateBlog

urlpatterns = [
    path("blogs/", CreateBlog.as_view()),
  ]
