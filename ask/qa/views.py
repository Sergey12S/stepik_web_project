from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from qa.models import Question, Answer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from qa.forms import AskForm, AnswerForm


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

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            _ = form.save()
            url = _.question
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()

    return render(request, 'question.html', {'question': question, 'answers': answers, 'form' : form})


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



def ask_page(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
        return render(request, 'ask.html', {
            'form' : form})
