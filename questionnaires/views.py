from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, GenericViewSet

from questionnaires.models import Questionnaire, UserConversation, UserInput
from questionnaires.serializers import QuestionnarieSerializer, UserConversationSerializer, UserInputSerializer, \
    UserConversationSerializerSimple


class QuestionnairesViewSet(ReadOnlyModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnarieSerializer


class UserConversationsViewSet(mixins.CreateModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.ListModelMixin,
                               GenericViewSet):
    queryset = UserConversation.objects.all()

    # serializer_class = UserConversationSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return UserConversationSerializer
        return UserConversationSerializerSimple


class UserInputsViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = UserInput.objects.all()
    serializer_class = UserInputSerializer
