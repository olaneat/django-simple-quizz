from django.urls import path
from .views import StoryDetail, StoryList
from . import views 

app_name = 'story'
urlpatterns = [

    path('', views.index, name="index" ),
    path('<int:id>/detail', views.storyDetail, name="detail")
]
