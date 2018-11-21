import json

from django.core.management import BaseCommand
from django.db import transaction

from questionnaires.models import Questionnaire, QuestionNode, AnswerVariant

EXAMPLE = {
    'question': 'Are you hungry?',
    'answer_variants': {
        'Yes': {
            'question': 'What would you like to eat?',
            'answer_variants': {
                'Hamburger': {
                    'question': 'Nice, I will order a hamburger for you!',
                    'answer_variants': None
                },
                'Pizza': {
                    'question': 'Would you like pizza with mushrooms?',
                    'answer_variants': {
                        'Yes': {
                            'question': 'Ok, I will order the best pizza in town for you',
                            'answer_variants': None
                        },
                        'No': {
                            'question': 'No? Well... stay hungry then',
                            'answer_variants': None
                        }
                    }
                },
            }
        },
        'No': {
            'question': 'Ok. Call me when you\'re hungry.',
            'answer_variants': None
        }
    }
}


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-p', '--path', type=str, help='Json File Path')
        parser.add_argument('-n', '--name', type=str, help='Questionnaire title')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        desc = kwargs['name']
        with open(path, 'r') as f:
            data = json.load(f)
        with transaction.atomic():
            q = Questionnaire(description=desc, root_node=self.traverse_questionnaire_json(data))
            q.save()

    def traverse_questionnaire_json(self, questionnaire: dict) -> QuestionNode:
        """
        Receives a json with question and answer_variants keys. Traverses the json tree recursivly
        populating the database
        :param questionnaire: json like structure
        :return: current question node created
        """
        question = QuestionNode(text=questionnaire['question'])
        question.save()
        if questionnaire['answer_variants'] is not None:
            for answer_variant, tree in questionnaire['answer_variants'].items():
                av = AnswerVariant(text=answer_variant,
                                   parent_question=question,
                                   next_question=self.traverse_questionnaire_json(tree))
                av.save()
        return question
