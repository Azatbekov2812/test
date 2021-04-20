from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import serializers

from .models import Question, Quiz, Choice, Answer

User = get_user_model()


class ActiveQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('start_date',)


class CreateQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'name', 'end_date', 'description')


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('options',)


class ChoicePrimaryKeyRelated(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        question_id = self.context.get('request').parser_context['kwargs']['question_id']
        request = self.context.get('request', None)
        queryset = super(ChoicePrimaryKeyRelated,
                         self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(question_id=question_id)


class AnswerSerializer(serializers.ModelSerializer):
    some_choice = ChoicePrimaryKeyRelated(many=True, queryset=Choice.objects.all())

    class Meta:
        fields = '__all__'
        model = Answer


class AnswerOneTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text', 'id_answer_user']


class AnswerOneChoiceSerializer(serializers.ModelSerializer):
    one_choice = ChoicePrimaryKeyRelated(
        many=False,
        queryset=Choice.objects.all()
    )

    class Meta:
        model = Answer
        fields = ['one_choice', 'id_answer_user']


class TagSerializer(serializers.RelatedField):
    class Meta:
        model = Choice


class AnswerMultipleChoiceSerializer(serializers.ModelSerializer):
    some_choice = ChoicePrimaryKeyRelated(many=True,
                                          queryset=Choice.objects.all()
                                          )

    class Meta:
        fields = ['some_choice', 'id_answer_user']
        model = Answer


# вопросы с ответами пользователей
# class QuestionListSerializer(serializers.ModelSerializer):
#     answers = serializers.SerializerMethodField('get_answers')
#
#     class Meta:
#         fields = ['question_text', 'answers']
#         model = Question
#
#     def get_answers(self, question):
#         # author_id = self.context.get('request').parser_context['kwargs']['id']
#         author_id = self.context.get('request').user.id
#         answers = Answer.objects.filter(
#             Q(question=question) & Q(id_answer_user=1))
#         serializer = AnswerSerializer(instance=answers, many=True)
#         return serializer.data


class UserQuizSerializer(serializers.ModelSerializer):
    questions = QuestionsSerializer(read_only=True, many=True)

    class Meta:
        fields = '__all__'
        model = Quiz
