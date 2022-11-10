from .models import Submission
from utils.api import serializers

class CreateAnswerSerializer(serializers.Serializer):
    created_by = serializers.IntegerField(null=False)
    content = serializers.CharField(allow_blank=True, allow_null=True)
    submission_id = serializers.IntegerField(null=False)
    question_id = serializers.IntegerField(null=False)