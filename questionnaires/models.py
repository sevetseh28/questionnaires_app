import uuid
from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
from django.db.models import DO_NOTHING, CASCADE


# Conversations
class QuestionNode(models.Model):
    text = models.CharField(max_length=1024)


class AnswerVariant(models.Model):
    text = models.CharField(max_length=1024)
    parent_question = models.ForeignKey(QuestionNode, on_delete=CASCADE, related_name='answer_variants')
    next_question = models.ForeignKey(QuestionNode, on_delete=CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.parent_question.answer_variants.count() < 5:
            super(AnswerVariant, self).save()
        else:
            raise Exception(f'{self.parent_question.text} has already 5 answer variants. No more are allowed.')


class Questionnaire(models.Model):
    description = models.CharField(max_length=1024)
    root_node = models.ForeignKey(QuestionNode, on_delete=CASCADE)  # Defines de conversation tree


# Conversations instances
class UserConversation(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, primary_key=True)
    questionnarie = models.ForeignKey(Questionnaire, on_delete=CASCADE, related_name='conversations')

    def __str__(self):
        return f'{self.questionnarie.root_node.text}: {" -> ".join([x.text for x in self.user_inputs.order_by("date")])}'


class UserInput(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    current_node = models.ForeignKey(QuestionNode, on_delete=CASCADE, default=None, null=True)
    conversation = models.ForeignKey(UserConversation, on_delete=CASCADE, related_name='user_inputs')
    text = models.CharField(max_length=1024)
