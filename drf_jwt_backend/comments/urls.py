from importlib.resources import path
from django.urls import path
from comments import views


urlpatterns = [
  path('comments/<str:video_id>/', views.get_all_comments),
  path('comment/create/', views.create_comment),
  # path('api/replies/', views.ReplyList.as_view())
]