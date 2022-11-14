from utils.api import APIView, validate_serializer
from account.decorators import login_required
from account.models import User
from ..models import Answer
from ..serializers import CreateAnswerSerializer
from question.models import Question

class AnswerAPI(APIView):
    # @validate_serializer(CreateAnswerSerializer)
    @login_required
    def post(self, request):
        data = request.data

        _created_by = User.objects.get(user_name=request.username)

        answer = answer.objects.create(
            created_by = _created_by,
            submission_id = data["submission_id"],
            content = data["content"],
            question_id = data["question_id"],

        )
        answer.save()

        question = Question.objects.get(id=data["question_id"])
        question.answer_registered = True
        question.answer_id = answer.id
        question.save()

        return self.success({"answer_id" : answer.id})

    def get(self, request):
        try:
             answer = Answer.objects.get(id=request.GET.get("id"))
        except Answer.DoesNotExist:
            return self.error("Invalid Answer ID")
        return self.success(answer)