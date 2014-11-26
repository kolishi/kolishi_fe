from django.http.response import HttpResponse
from conference.models import Counter
from django.contrib.gis.geoip import GeoIP


__author__ = 'tal'
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django_twilio.client import twilio_client
PHONE_NUMERS = { "IL" : "97243748620",
                 "GB" : "+441702680287",
                 "US" : "+15167084158"
}

def country_to_origin_number(Country_code):
    return PHONE_NUMERS.get(Country_code,PHONE_NUMERS["US"])

def UpdateConferenceSerial():
    NumberOfCalls =Counter.objects.get_or_create(pk=1)[0]
    ConferenceName = Counter.objects.get_or_create(pk=2)[0]
    if NumberOfCalls.Count % 2 == 0 :
        ConferenceName.Count = NumberOfCalls.Count /2
        ConferenceName.save()
    NumberOfCalls.Count +=1
    NumberOfCalls.save()

def call(num,origin_number):
    UpdateConferenceSerial()
    ConferenceName = Counter.objects.get_or_create(pk=2)[0].Count
    c = twilio_client.calls.create(to=num, from_ = origin_number,
            url="https://twimlets.com/conference?Name=conf_{0}".format(ConferenceName)
    )
    return c

class NameForm(forms.Form):
    Caller = forms.CharField(label='Enter Your phone number (eg +14156634567)\n', max_length=100)

class PhoneNumberForm(forms.Form):

    CountryCode = forms.IntegerField(label="Country Code",widget=forms.TextInput(attrs={'size': '3'}),initial=1)
    AreaCode = forms.IntegerField(label="Area Code",widget=forms.TextInput(attrs={'size': '3'}),initial=800)
    PhoneNumber = forms.IntegerField(label="Phone Number",widget=forms.TextInput(attrs={'size': '10'}),initial=5555555)
    def get_number(self):
        return "+{0}{1}{2}".format(self.cleaned_data["CountryCode"],
                                   self.cleaned_data["AreaCode"],
                                   self.cleaned_data["PhoneNumber"]
                            )
def thanks(request,*args):
    text =request.POST

    return HttpResponse("Calling")

def conf(call,city):
    ConferenceName = Counter.objects.get_or_create(pk=2)[0].Count
    return HttpResponse(

        "Call status is {0} ".format(ConferenceName)
    )

    return HttpResponse(text)
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PhoneNumberForm(request.POST)


        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            g = GeoIP()
            ip = get_client_ip(request)
            if ip:
                country = g.country(ip)['country_code']
            else:
                country = 'Rome' # default city
            origin_number =country_to_origin_number(country)
            c= call(form.get_number(),origin_number)
            # redirect to a new URL:
            return conf(c,country)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PhoneNumberForm()


    return render(request, 'index.html', {'form': form})