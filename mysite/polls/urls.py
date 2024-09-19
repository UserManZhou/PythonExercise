from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results", views.results, name="results"),
    path("<int:question_id>/vote", views.vote, name="vote"),
    path("articles/2003/", views.specific_case_2003, name="specific_case_2003"),
    path("articles/<int:year>/", views.year_archive, name="year_archive"),
    path("articles/<int:year>/<int:month>/", views.month_archive, name="month_archive"),
    path("articles/<int:year>/<int:month>/<slug:slug>/", views.article_detail, name="article_detail")
]
