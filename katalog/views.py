from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    catalog_data = CatalogItem.objects.all()
    context = {
    'catalog_data': catalog_data,
    'nama': 'Rahmat Bryan Naufal',
    'npm': '2106635650'
    }
    return render(request, "katalog.html", context)
