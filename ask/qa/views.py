from django.shortcuts import render

from django.http import HttpResponseRedirect, Http404
from django.core.paginator import Paginator
from qa.models import Question

# Create your views here.

from django.http import HttpResponse 

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def index(request):
    try:
        page = int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    questions = Question.objects.all().order_by('-id')
    paginator = Paginator(questions, 10)
    page = paginator.page(page)

    return render(request, 'list.html',
                  {'title': 'Latest',
                   'paginator': paginator,
                   'questions': page.object_list,
                   'page': page,
                   'user': request.user,
                   'session': request.session, })

def popular(request):
    try:
        page = int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    questions = Question.objects.all().order_by('-rating')
    paginator = Paginator(questions, 10)
    page = paginator.page(page)

    return render(request, 'list.html',
                  {'title': 'Popular',
                   'paginator': paginator,
                   'questions': page.object_list,
                   'page': page,
                   'user': request.user,
                   'session': request.session, })

def question(request, num,):
    try:
        q = Question.objects.get(id=num)
    except Question.DoesNotExist:
        raise Http404
    
    return render(request, 'question.html', {'question': q,
                                             
                                             'user': request.user,
                                             'session': request.session, })
