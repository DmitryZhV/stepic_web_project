
# Create your views here.
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET
from qa.models import Question, Answer

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def article(request):
    id = request.GET.get('page') 
        
    
    print(id)
    return render_to_response('index.html', {

        })
@require_GET
def question(request, id):
    question=get_object_or_404(Question, id=id)
    try:
        AsText=Answer.objects.filter(question_id=id)
    except Answer.DoesNotExist:
        AsText=None
    return render(request, 'question.html', {
        'question': question,
        'astext' : AsText,
    })

def popular(request):
    try:
        page=int(request.GET.get('page'))
    except ValueError:
        page=1
    except TypeError:
        page=1
    
    question=Question.objects.all().order_by('-rating')
    paginator=Paginator(question, 10)
    paginator.baseurl='question/'
    page=paginator.page(page)
    return render(request,'questions_list.html' , {
                  'title': 'Popular Question',
                  'question': page.object_list,
                  'paginator': paginator, 
                  'page': page,
                  })
    


def main(request):
    try:
        page=int(request.GET.get('page', 1))
    except ValueError:
        page=1
    except TypeError:
        page=1
    
    question=Question.objects.all().order_by('-id')
    #limit=request.GET.get('limit',10)
    paginator=Paginator(question, 10)
    paginator.baseurl='question/'
    page=paginator.page(page)
    return render(request,'questions_list.html' , {
                  'title': 'Last Question',
                  'question': page.object_list,
                  'paginator': paginator, 
                  'page': page,
                  })
    
    
    