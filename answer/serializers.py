from utils.api import serializers
from utils.api._serializers import UsernameSerializer

class CreateAnswerSerializer(serializers.Serializer):
    created_by = UsernameSerializer()
    content = serializers.CharField(allow_blank=True, allow_null=True)
    submission_id = serializers.IntegerField(allow_null=True)
    question_id = serializers.IntegerField(allow_null=True)