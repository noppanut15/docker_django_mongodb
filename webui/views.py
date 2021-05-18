from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from webui.models import *

def index(request):
    all_contacts = Contacts.objects.all()
    # print(all_contacts)
    for i in all_contacts:
        print(i.firstName)
    context = {

    }
    return render(request, 'index.html', context)