from django.http import HttpResponse
from  django.shortcuts import render

def about(reguest):
    return HttpResponse('Portfolio')


def home(regust):
    return render(regust, 'home.html',
                  {'helo':'Привет!',
                   'bye':'Пока'})