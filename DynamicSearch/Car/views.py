from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import *


def index(request):
    return render(request, 'Car/base.html', context={})



class SearchField(View):
    model = Car
    template = 'Car/search.html'
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            search = request.POST['search']
        else:
            search = ''
        cars = self.model.objects.filter(name__icontains=search)
        context = {
            'cars':cars
        }
        return render(request, self.template, context)
