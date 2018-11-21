from rest_framework import serializers

from questionnaires.models import Questionnaire, UserConversation, UserInput, QuestionNode, AnswerVariant


class AnswerVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerVariant
        fields = ('text',)


class QuestionNodeSerializer(serializers.ModelSerializer):
    answer_variants = AnswerVariantSerializer(many=True)

    class Meta:
        model = QuestionNode
        fields = '__all__'


class QuestionnarieSerializer(serializers.ModelSerializer):
    root_node = QuestionNodeSerializer(many=False)

    class Meta:
        model = Questionnaire
        fields = '__all__'


class UserConversationSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    questionnarie = QuestionnarieSerializer(read_only=False)

    class Meta:
        model = UserConversation
        fields = ('id', 'questionnarie')


class UserConversationSerializerSimple(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = UserConversation
        fields = ('id', 'questionnarie')


class UserInputSerializer(serializers.ModelSerializer):
    current_node = QuestionNodeSerializer(many=False, read_only=True)

    class Meta:
        model = UserInput
        fields = '__all__'

    def create(self, validated_data):
        conv = validated_data['conversation']
        if conv.user_inputs.count() == 0:  # means it is the first user message
            current_state_node = conv.questionnarie.root_node
        else:
            latest_user_input = conv.user_inputs.latest('date')
            current_state_node = latest_user_input.current_node

        answer_variants_available = current_state_node.answer_variants.all()
        text = validated_data['text']
        try:  # Check that the user input is a valid answer variant for the current node of conversation
            answer_variant: AnswerVariant = answer_variants_available.get(text=text)
            current = answer_variant.next_question
            userinput = UserInput(**validated_data, current_node=current)
            userinput.save()
            # Check if this is the last node of conversation, if it is, then log it
            if not current.answer_variants.exists():
                print(conv)
            return userinput
        except AnswerVariant.DoesNotExist:
            raise serializers.ValidationError(f'{text} is not a possible answer variant')
