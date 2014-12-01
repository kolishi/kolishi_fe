PHONE_NUMERS = { "IL" : "97243748620",
                 "GB" : "+441702680287",
                 "US" : "+15167084158"
}

def country_to_origin_number(Country_code):
    return PHONE_NUMERS.get(Country_code,PHONE_NUMERS["US"])

def UpdateConferenceSerial():
    NumberOfCalls =Counter.objects.get_or_create(pk=1)[0]
    ConferenceName = Counter.objects.get_or_create(pk=2)[0]
    NumberOfCalls.Count +=1
    ConferenceName.Count = NumberOfCalls.Count
    ConferenceName.save()

    NumberOfCalls.save()

def call(num,origin_number):

    ConferenceName = Counter.objects.get_or_create(pk=2)[0].Count
    c = twilio_client.calls.create(to=num, from_ = origin_number,
            url="http://twimlbin.com/external/e0bc03ea6ef18cd5?Name=conf_{0}".format(ConferenceName)
    )
    return c

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip