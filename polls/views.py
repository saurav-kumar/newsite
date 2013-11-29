# Create your views here.
from django.http import HttpResponse
from polls.models import Poll
#from django.template import Context, loader

from django.shortcuts import render_to_response, get_object_or_404
#Note no need to import Context and loader after importing this.
#thus we can return the page like:
# return render_to_response('path_to_template', {context}) ; see below

def index(request):
    ''' The index view, which will show all the polls'''

    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    '''now it contains first 5 latest poll.'''

    '''t = loader.get_template('polls/index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,
        'User': 'Saurav Kumar'
    })

    return HttpResponse(t.render(c))
    '''

    return render_to_response('polls/index.html', {
        'latest_poll_list': latest_poll_list,
        'User': 'Saurav Kumar'
        })

    #output = ', '.join([p.question for p in latest_poll_list])
    #return HttpResponse(output)


def detail(request, poll_id):
    '''This function is to display the details of the indivisual polls'''
    
    p = get_object_or_404(Poll, pk = poll_id)
    ''' This method will get the object(Poll) bases on the its id'''
    
    return render_to_response('polls/detail.html', {
        'poll': p,
        'User': 'Saurav Kumar'
        })
    '''Give special attention to this function. Get help from index() above'''

def vote(request, choice_id):
    return 'Hello!'

def results(request, poll_id):
    return 'Hello!'
