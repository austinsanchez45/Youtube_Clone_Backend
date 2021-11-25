from django.urls import path
from . import views

urlpatterns = [
    path('youtube_app', views.YoutubeList.as_view()),
    path('youtube_app/<int:pk>', views.Comments.as_view()),
    path('youtube_app/likes/<int:pk>', views.Like.as_view()),
    path('youtube_app/dislikes/<int:pk>', views.Dislike.as_view())

]
