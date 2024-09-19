from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from sqlparse.tokens import Number


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def specific_case_2003(request):
    return HttpResponse("Hello, world. You're at the " + str(request.body) + " index.")


def year_archive(request, year):
    return HttpResponse("Hello, world. You're at the " + str(year) + " index.")


def month_archive(request, year, month):
    return HttpResponse("Hello, world. You're at the " + str(year) + str(month) + " index.")


def article_detail(request, year, month, slug):
    return HttpResponse("Hello, world. You're at the " + str(year) + str(month) + str(slug) + " index.")
