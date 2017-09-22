from django.shortcuts import render
from django.http import HttpResponse, Http404
from qa.models import Question, Answer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def home_page(request):
    questions = Question.objects.new()
    paginator = Paginator(questions, 10)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'questions': questions})


def question_page(request, id):
    try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
        raise Http404
    answers = Answer.objects.filter(question=id)
    return render(request, 'question.html', {'question': question, 'answers': answers})


def popular_page(request):
    questions = Question.objects.popular()
    paginator = Paginator(questions, 10)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'popular.html', {'questions': questions})

