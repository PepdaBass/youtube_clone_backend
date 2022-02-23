from importlib.resources import path
from django.urls import path
from comments import views


urlpatterns = [
  path('comments/<str:video_id>/', views.get_video_comments),
  path('comment/create/', views.create_comment),
  path('comment/edit/<int:pk>/', views.edit_comment),
  path('replies/<int:comment_id>/', views.get_comment_replies),
  path('reply/', views.create_reply)
]