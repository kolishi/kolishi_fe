from django.http.response import HttpResponse
from conference.models import Counter
from django.contrib.gis.geoip import GeoIP
from confession.redis_conference_wrapper import AddNumberAndGetPair
from django.shortcuts import render
from forms import PhoneNumberForm
from utilities import  call,get_client_ip,country_to_origin_number,UpdateConferenceSerial
from django import forms
from xml.dom import ValidationErr
__author__ = 'tal'



def thanks(request,*args):
    text =request.POST

    return HttpResponse("Calling")

def conf(call,city):
    #ConferenceName = Counter.objects.get_or_create(pk=2)[0].Count
    return HttpResponse(

        "Kolishi will call you soon with someone to talk to "
    )

    return HttpResponse(text)



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PhoneNumberForm(request.POST)

        # check whether it's valid:
        try:

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

                NumPair = AddNumberAndGetPair(form.get_number())

                if NumPair.ready == True:
                    c= call(NumPair.ToNumber1,NumPair.FromNumber1)
                    c= call(NumPair.ToNumber2,NumPair.FromNumber2)
                    UpdateConferenceSerial()
                # redirect to a new URL:
                c = None
                return conf(c,country)

        except ValidationErr,e:
                raise Exception(request.POST)


    # if a GET (or any other method) we'll create a blank form
    else:
        form = PhoneNumberForm()


    return render(request, 'index.html', {'form': form})