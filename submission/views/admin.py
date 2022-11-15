from account.decorators import super_admin_required
from judge.tasks import judge_task
# from judge.dispatcher import JudgeDispatcher
from utils.api import APIView
from ..models import Submission
from problem.models import Problem

import requests


class SubmissionRejudgeAPI(APIView):
    @super_admin_required
    def get(self, request):
        id = request.GET.get("id")
        if not id:
            return self.error("Parameter error, id is required")
        try:
            submission = Submission.objects.select_related("problem").get(id=id, contest_id__isnull=True)
        except Submission.DoesNotExist:
            return self.error("Submission does not exists")
        submission.statistic_info = {}
        submission.save()

        judge_task.send(submission.id, submission.problem.id)
        return self.success()

class SubmissionVisualDataResultAPI(APIView):
    def get(self, request):
        ## Get Code
        submission_id = request.GET.get("submission_id")
        submission = Submission.objects.get(id=submission_id)
        code = submission.code

        ##Get input Case
        problem_id = request.GET.get("problem_id")
        problem = Problem.objects.get(id=problem_id)
        inputDescription = problem.input_description

        ## 추후에 윤석이랑 연결되면 URL 넣어서 사용 예정
        response = requests.get("넣을 URL", data = {"code" : code, "input_description" : inputDescription})

        return self.success(response)
