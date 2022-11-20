from django.shortcuts import render
from testing.models import people, goods
from testing.forms import *
from django.http import HttpResponseRedirect


# Create your views here.

def homeview(request):
    quieryset = goods.objects.all()
    person    = people.objects.all()
    context = {
        'quieryset': quieryset,
        'person': person
    }
    return render(request, 'index.html', context)


def detailview(request, id):
    item  = goods.objects.get(id=id)
    context  = {
        'item': item
    }
    return render(request, 'detail.html', context)

def adding_good(request):
    form = adding_goods()

    if request.method == 'POST':
        form = adding_goods(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/thanks/')
    
    context = {
        'form': form
    }

    return render(request, 'addingform.html', context)

def thankView(request):
    return render(request, 'thanks.html')
