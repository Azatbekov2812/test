from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken

from . import views

router = DefaultRouter()

router.register('quiz', views.QuizViewSet, basename='quiz')
router.register(r'quiz/(?P<quiz_id>\d+)/questions', views.QuestionViewSet, basename='questions')
router.register(r'quiz/(?P<quiz_id>\d+)/questions/(?P<question_id>\d+)/choices', views.ChoiceViewSet,
                basename='choices')
router.register(r'quiz/(?P<quiz_id>\d+)/questions/(?P<question_id>\d+)/answers', views.AnswerCreateViewSet,
                basename='answers')

router.register(r'user_quiz/(?P<user_id>\d+)', views.UserQuizViewSet, basename='user_quiz')  # list quizdetail

#router.register('activate', views.ActivateQuiz, basename='activate')  # start quiz date
router.register('active_quiz', views.ActiveQuizViewSet, basename='active_quiz')

urlpatterns = [
    path('', include(router.urls)),
    path('jwt_token/', ObtainJSONWebToken.as_view()),
    path('refresh_token/', RefreshJSONWebToken.as_view()),
]
