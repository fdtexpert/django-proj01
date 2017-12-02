from django.shortcuts import render
from django.http import HttpResponse
from amtesting_app.models import AccessRecord,WebPage,Topic
# Create your views here.

def index(request):
#    return HttpResponse("Hello WOrld!!!")
    webpages_list = AccessRecord.objects.order_by('date')
    my_arg = {'insert_me': 'This is Argument Amir 01 - New Test', 'access_records': webpages_list}

    return render(request,'amtesting_app/index.html',context=my_arg)
