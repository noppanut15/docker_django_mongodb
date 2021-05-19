from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from webui.utils import get_db_handle, get_collection_handle

def index(request):
    db_handle, mongo_client = get_db_handle()
    collection_handle = get_collection_handle(db_handle, "contacts")
    data = collection_handle.find({'firstName': 'James'})
    for x in data:
        print(x['firstName'])

    context = {

    }

    return render(request, 'index.html', context)