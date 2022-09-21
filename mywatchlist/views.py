from django.shortcuts import render
from mywatchlist.models import WatchItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_xml_by_id(request, id):
    data = WatchItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = WatchItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json(request):
    data = WatchItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = WatchItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_mywatchlist(request):
    watch_data = WatchItem.objects.all()
    context = {
        'watch_data': watch_data,
        'nama': 'Rahmat Bryan Naufal',
        'npm': '2106635650'
    }
    return render(request, "katalog.html", context)
