from importlib.resources import path
from django.urls import path
from comments import views


urlpatterns = [
  path('api/comments/', views.CommentList.as_view()),
  path('api/replies/', views.ReplyList.as_view())
]