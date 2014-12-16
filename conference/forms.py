from django.http import HttpResponseRedirect
from django_twilio.client import twilio_client
from django import forms
from xml.dom import ValidationErr
class NameForm(forms.Form):
    Caller = forms.CharField(label='Enter Your phone number (eg +14156634567)\n', max_length=100)

class PhoneNumberForm(forms.Form):

    CountryCode = forms.IntegerField(label="Country Code",widget=forms.NumberInput(attrs={'size': '3','class':'test'} ))
    AreaCode = forms.IntegerField(label="Area Code",widget=forms.NumberInput(attrs={'size': '3'}))
    PhoneNumber = forms.IntegerField(label="Phone Number",widget=forms.NumberInput(attrs={'size': '10'}))
    def get_number(self):
        return "+{0}{1}{2}".format(self.cleaned_data["CountryCode"],
                                   self.cleaned_data["AreaCode"],
                                   self.cleaned_data["PhoneNumber"]
                            )

    def clean(self):
        pass
