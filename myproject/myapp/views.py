from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World Test 12345678910!")