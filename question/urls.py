from django.urls import path
from . import views

app_name="question"
urlpatterns = [
    path('', views.questionIndex, name="home" ),
    path("result", views.finalResult, name="finalResult")
]
