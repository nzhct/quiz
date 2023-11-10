from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('quiz', views.quiz, name='quiz'),
    path('api/get-quiz/', views.get_quiz, name='get_quiz'),
]