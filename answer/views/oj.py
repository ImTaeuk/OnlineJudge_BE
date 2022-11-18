from utils.api import APIView, validate_serializer
from account.decorators import login_required
from account.models import User
from ..models import Answer
from question.models import Question

class AnswerAPI(APIView):
    # @validate_serializer(CreateAnswerSerializer)
    # @login_required
    def post(self, request):
        data = request.data

        question = Question.objects.get(id=data["question_id"])
        
        if (question.answer_registered):
                answer = Answer.objects.get(question_id=data["question_id"])
                answer.content = data["content"]
                answer.save()
                return self.success({"answer_question_id" : answer.question_id})
            

        _created_by = User.objects.get(username=data["username"])

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

        return self.success({"answer_question_id" : answer.question_id})

    def get(self, request):
        data = request.data
        
        try:
             answer = Answer.objects.get(id=request.GET.get("id"))
        except Answer.DoesNotExist:
            return self.error("등록된 답변이 없습니다.")
        
        return self.success({"answer_id" : answer.id, "content" : answer.content, "submission_id" : answer.submission_id, "question_id" : answer.question_id})