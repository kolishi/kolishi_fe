from django.http.response import HttpResponse

__author__ = 'tal'
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django_twilio.client import twilio_client
NumberOfCalls =0
ConferenceName =0

def UpdateConferenceSerial():
    global NumberOfCalls
    global ConferenceName
    if NumberOfCalls % 2 == 0 :
        ConferenceName = NumberOfCalls /2
    NumberOfCalls +=1

def call(num):
    global ConferenceName
    UpdateConferenceSerial()
    c = twilio_client.calls.create(to=num, from_ = "+97243748620",
            url="https://twimlets.com/conference?Name=conf_{0}".format(ConferenceName)
    )
    return c

class NameForm(forms.Form):
    Caller = forms.CharField(label='Enter Your phone number (eg +14156634567)\n', max_length=100)

def thanks(request,*args):
    text =request.POST

    return HttpResponse("Calling")

def conf(call):
    return HttpResponse(
        "Call status is {0}".format(ConferenceName)
    )

    return HttpResponse(text)

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)


        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            c= call(form.cleaned_data["Caller"])
            # redirect to a new URL:
            return conf(c)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()


    return render(request, 'name.html', {'form': form})