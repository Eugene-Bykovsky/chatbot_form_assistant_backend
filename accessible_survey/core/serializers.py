from rest_framework import serializers

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    options_list = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id', 'text', 'q_type', 'options_list', 'required', 'hint']

    def get_options_list(self, obj):
        return obj.get_options_list()
