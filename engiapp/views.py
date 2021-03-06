# Create your views here.

from django.core import serializers
from django.shortcuts import render_to_response
from django.template import RequestContext 
from django.contrib.auth import logout
from django.http import *
from engiapp.forms import *
from engiapp.models import *
import json
from random import choice
from string import letters
from django.shortcuts import render_to_response , get_object_or_404

def main_page(request): 
    	variables = RequestContext(request, {})
    	return render_to_response('main_page.html', variables) 



def logout_page(request):
    logout(request) #invalidates the user session
    return HttpResponseRedirect('/') 



def register_page(request):
    if request.method == 'POST': #user has submitted the form
        form = RegistrationForm(request.POST)
        if form.is_valid():
	    username=''.join([choice(letters) for i in xrange(30)])
            user = User.objects.create_user( username=username,first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'], password=form.cleaned_data['password1'], email=form.cleaned_data['email'])

	    student=Student(user=user,date_of_birth=form.cleaned_data['date_of_birth'],country=form.cleaned_data['country'],state=form.cleaned_data['state'],city=form.cleaned_data['city'],address=form.cleaned_data['address'],institution_name=form.cleaned_data['institution_name'])
	    student.save()
	    return HttpResponseRedirect('/register/success/') 
    else: 
        form = RegistrationForm() 
    variables = RequestContext(request, {'form': form }) 
    return render_to_response('registration/register.html', variables ) 

def all_committee(request):
    return HttpResponse(serializers.serialize("json", Committee.objects.all()))

def committee(request,committee_id):
    return HttpResponse(serializers.serialize("json",EngiEvents.objects.filter(pk=committee_id)))

def all_events(request):
    # response_data = EngiEvents.objects.all()
    return HttpResponse(serializers.serialize("json", EngiEvents.objects.all()))    

def event(request,event_id):
    # p = get_object_or_404(EngiEvents , pk=event_id)
    return HttpResponse(serializers.serialize("json",EngiEvents.objects.filter(pk=event_id)))