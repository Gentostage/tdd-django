from django.shortcuts import render, redirect
from django.http import HttpResponse

from lists.models import Item


def home_page(request):
    '''Домашняя сраница'''
    return render(request, 'home.html')

def view_list(request):
    '''представление списка'''
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/single-lice-in-world/')