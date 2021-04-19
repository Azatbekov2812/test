from django.contrib import admin
from django.urls import path
from .views import QuestionList, QuizList, QuizDetail, QuestionDetail

urlpatterns = [
    path('quiz/', QuizList.as_view()),
    path('quiz/<int:pk>/', QuizDetail.as_view()),
    path('questions/', QuestionList.as_view()),
    path('questions/<int:pk>/', QuestionDetail.as_view()),
]
