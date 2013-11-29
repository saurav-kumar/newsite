# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Poll, Choice
from django.template import RequestContext # Added in part 4 for vote()
from django.core.urlresolvers import reverse # Added in part 4 for vote()
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
        'User': 'Saurav Kumar',
        },
        context_instance=RequestContext(request))
    '''Give special attention to this function. Get help from index() how
    previous template and context are used now '''

def vote(request, poll_id):
    ''' this function is used to increment the vote count for Poll's selected choice'''
    
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        '''Redisplay the poll voting form.'''
        return render_to_response('polls/detail.html', {
            'poll': p,
            'User': 'Saurav Kumar',
            'error_message': "Please select a choice first.",
            }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))


def results(request, poll_id):
    p = get_object_or_404(Poll, pk = poll_id)
    return render_to_response('polls/results.html', {
        'poll': p,
        'User': 'Saurav Kumar',
        })
