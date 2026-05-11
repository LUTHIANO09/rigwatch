from django.http import HttpResponse
import datetime

# Create your views here.
def home(request):
    date = datetime.datetime.now()
    return HttpResponse(f'<h1> Welcome to Rigwatch </h1> {date}')