from django.db.models import Q
from rest_framework import status, permissions
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Question, Quiz, Choice, Answer
from .serializers import QuestionsSerializer, QuizSerializer, ActiveQuizSerializer, ChoiceSerializer, AnswerSerializer, \
    AnswerOneTextSerializer, AnswerOneChoiceSerializer, AnswerMultipleChoiceSerializer, UserQuizSerializer


# Create your views here.
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAdminUser]


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionsSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        quiz = get_object_or_404(Quiz, id=self.kwargs['quiz_id'])
        return Question.objects.filter(quiz=quiz)

    def create(self, request, *args, **kwargs):
        quiz = get_object_or_404(Quiz, id=self.kwargs['quiz_id'])
        if quiz.start_date:
            return Response('quiz start date not null', status=status.HTTP_204_NO_CONTENT)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAdminUser]


class AnswerCreateViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            questions = get_object_or_404(Question, pk=self.kwargs['question_id'], quiz__id=self.kwargs['quiz_id'])
            if questions.type == Question.TYPE_TEXT:
                return AnswerOneTextSerializer
            elif questions.type == Question.TYPE_ONE:
                return AnswerOneChoiceSerializer
            else:
                return AnswerMultipleChoiceSerializer

        else:
            return AnswerSerializer

    def perform_create(self, serializer):
        question = get_object_or_404(
            Question,
            id=self.kwargs['question_id'],
            quiz__id=self.kwargs['quiz_id'],
        )
        serializer.save(user=self.request.user, question=question)


class UserQuizViewSet(viewsets.ModelViewSet):
    serializer_class = UserQuizSerializer

    def get_queryset(self):
        id_answer_user = self.kwargs['user_id']
        #return Question.objects.filter(answers__id_answer_user=id_answer_user)
        return Quiz.objects.filter(questions__answers__user_id=id_answer_user)


class ActiveQuizViewSet(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.customObject.active()
    http_method_names = ['get']


class ActivateQuiz(viewsets.ModelViewSet):
    serializer_class = ActiveQuizSerializer
    queryset = Quiz.customObject.yet_not_active()
