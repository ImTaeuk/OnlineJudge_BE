from django.conf.urls import url

from ..views.admin import SubmissionRejudgeAPI, SubmissionVisualDataResultAPI

urlpatterns = [
    url(r"^submission/rejudge?$", SubmissionRejudgeAPI.as_view(), name="submission_rejudge_api"),
    url(r"^submission/submissionVisualData?$", SubmissionVisualDataResultAPI.as_view(), name="submission_visual_data"),
]
