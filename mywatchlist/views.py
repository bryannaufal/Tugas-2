from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_mywatchlist(request):
    watch_data = MyWatchList.objects.all()
    sum_watched = MyWatchList.objects.filter(watched = True).count()
    sum_not_watched = MyWatchList.objects.filter(watched = False).count()
    if sum_watched>sum_not_watched:
        pesan = "Selamat, kamu sudah banyak menonton!"
    else:
        pesan = "Wah, kamu masih sedikit menonton!"
    context = {
        'watch_data': watch_data,
        'nama': 'Rahmat Bryan Naufal',
        'npm': '2106635650',
        'pesan': pesan
    }
    return render(request, "mywatchlist.html", context)
