from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Question, Quiz

User = get_user_model()


class CreateQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('name', 'description')


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class CreateQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('name', 'description')
