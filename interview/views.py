from django.shortcuts import render
from rest_framework import generics
from .models import Question, Quiz
from .serializers import QuestionsSerializer, CreateQuestionsSerializer, QuizSerializer, CreateQuizSerializer


# Create your views here.
class QuizList(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = CreateQuizSerializer


class QuizDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer
