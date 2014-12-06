from django.shortcuts import render
from conference.forms import PhoneNumberForm


def test(request):
    form = PhoneNumberForm()
    return render(request, 'bootstrap_template/index.html',{'form': form})
# Create your views here.
