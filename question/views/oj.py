from utils.api import APIView, validate_serializer
from account.decorators import login_required
from ..models import Question
from ..serializers import CreateQuestionSerializer
from account.models import User

class QuestionAPI(APIView):
    # @validate_serializer(CreateQuestionSerializer)
    # @login_required
    def post(self, request):
        data = request.data
        data["created_by"] = User.objects.get(username=data["username"])
        data["problem"] = data["problem_id"]
        createdUser = User.objects.get(username=data["username"])
        question = Question.objects.create(
            created_by = createdUser,
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

        result = {"id" : question.id, "class_id" : question.contest_id, "problem_id" : question.problem_id, "submission_id" : question.submission_id, "answer_id" : question.answer_id, "title" : question.title, "content" : question.content}
        
        return self.success(result)

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