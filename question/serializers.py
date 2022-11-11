from .models import Submission
from utils.api import serializers
from utils.serializers import LanguageNameChoiceField
from utils.api._serializers import UsernameSerializer

class CreateQuestionSerializer(serializers.Serializer):
    created_by = username = serializers.CharField(allow_null=True)
    title = serializers.CharField(max_length=256)
    problem_id = serializers.IntegerField(allow_null=True)
    contest_id = serializers.IntegerField(null=True)
    content = serializers.CharField(allow_blank=True, allow_null=True)
    submission_id = serializers.IntegerField(null=True)