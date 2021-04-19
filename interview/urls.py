from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views
from .views import QuestionList, QuizList, QuizDetail, QuestionDetail

router = DefaultRouter()

router.register('quiz', views.QuizViewSet, basename='quiz')
router.register(r'quiz/(?P<quiz_id>\d+)/questions', views.QuestionViewSet, basename='questions')
#router.register('quiz/<int:pk>/questions', views.QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('quiz/', QuizList.as_view()),
    # path('quiz/<int:pk>/', QuizDetail.as_view()),
    # path('quiz/<int:pk>/questions/', QuestionList.as_view()),
    # path('quiz/<int:quiz_id>/questions/<int:pk>/', QuestionDetail.as_view()),
]
