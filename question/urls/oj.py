from django.conf.urls import url
from ..views.oj import QuestionAPI, GetQuestionList

urlpatterns = [
    url(r"^question/question_list_api/?$", GetQuestionList.as_view(), name="get_question_list"),
    url(r"^question/question_api/?$", QuestionAPI.as_view(), name="question_api"),
]
