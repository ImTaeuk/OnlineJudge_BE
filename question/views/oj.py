from utils.api import APIView, validate_serializer
from account.decorators import login_required
from ..models import Question
from account.models import User
from ..serializers import CreateQuestionSerializer

class QuestionAPI(APIView):
    @validate_serializer(CreateQuestionSerializer)
    @login_required
    def post(self, request):
        data = request.data

        _created_by = User.objects.get(user_name=request.username)

        question = Question.objects.create(
            created_by = data["username"],
            title = data["title"],
            problem_id = data["problem_id"],
            contest_id = data["contest_id"],
            submission_id = data["submission_id"],
            content = data["content"],
            answer_id = None,
            answer_registered = False,
        )
        question.save()
        return self.success({"question_id" : question.id})

    def get(self, request):
        try:
             question = Question.objects.get(id=request.GET.get("id"))
        except Question.DoesNotExist:
            return self.error("Invalid Question ID")
        return self.success(question)

class GetQuestionList(APIView):
    def get(self, request):
        question_list = []
        questions = Question.objects.all()
        for v in questions:
            if v["answer_registered"] == False:
                answer_id = None
            else: answer_id = v["answer_id"]
            if v["created_by"] == request.user_id:
                question_list.append(
                    {
                        "question_id" : v["id"],
                        "class_id" : v["contest_id"], 
                        "problem_id" : v["problem_id"],
                        "title" : v["title"],
                        "answer_id" : answer_id
                    }
                 )
        return self.success(question_list)