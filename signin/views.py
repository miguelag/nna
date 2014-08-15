# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from signin.forms import PersonForm
from signin.models import Person


def index(request):
    peopleList = Person.objects.all()
    context = {'peopleList': peopleList}
    return render(request, 'signin/index.html', context)

def person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(request, 'signin/person.html', {'person': person})

def createPerson(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/signin')
    else:
	form=PersonForm()

    return render(request, 'signin/createPerson.html', {'form': form})
