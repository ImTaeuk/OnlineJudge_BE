from django.conf.urls import url

from ..views.oj import AnswerAPI

urlpatterns = [
    url(r"^answer/answer_api/?$", AnswerAPI.as_view(), name="answer_api"),
]

