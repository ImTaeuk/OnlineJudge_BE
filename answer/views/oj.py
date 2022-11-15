from utils.api import APIView, validate_serializer
from account.decorators import login_required
from account.models import User
from ..models import Answer
from question.models import Question

class AnswerAPI(APIView):
    # @validate_serializer(CreateAnswerSerializer)
    @login_required
    def post(self, request):
        data = request.data

        question = Question.objects.get(id=data["question_id"])
        
        if (question.answer_registered):
                answer = Answer.objects.get(question_id=data["question_id"])
                answer.content = data["content"]
                answer.save()
                return self.success(answer)
            

        _created_by = User.objects.get(user_name=request.username)

        answer = Answer.objects.create(
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

        return self.success(answer)

    def get(self, request):
        try:
             answer = Answer.objects.get(question_id=request.GET.get("question_id"))
        except Answer.DoesNotExist:
            return self.error("Invalid Answer ID")
        return self.success(answer)