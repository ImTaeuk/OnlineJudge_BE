from django.conf.urls import include, url

urlpatterns = [
    url(r"^api/", include("account.urls.oj")),
    url(r"^api/admin/", include("account.urls.admin")),
    url(r"^api/", include("announcement.urls.oj")),
    url(r"^api/admin/", include("announcement.urls.admin")),
    url(r"^api/", include("conf.urls.oj")),
    url(r"^api/admin/", include("conf.urls.admin")),
    url(r"^api/", include("problem.urls.oj")),
    url(r"^api/admin/", include("problem.urls.admin")),
    url(r"^api/", include("contest.urls.oj")),
    url(r"^api/admin/", include("contest.urls.admin")),
    url(r"^api/", include("submission.urls.oj")),
    url(r"^api/admin/", include("submission.urls.admin")),
    url(r"^api/admin/", include("question.urls.admin")),
    url(r"^api/", include("question.urls.oj")),
    url(r"^api/admin/", include("answer.urls.admin")),
    url(r"^api/", include("answer.urls.oj")),
    url(r"^api/admin/", include("utils.urls")),
]
