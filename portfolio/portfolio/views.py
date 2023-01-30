from django.http import HttpResponse
from  django.shortcuts import render

# def about(reguest):
#     return HttpResponse('Portfolio')
#
#
# def home(regust):
#     return render(regust, 'home.html',
#                   {'hello':'Привет!',
#                    'bye':'Пока'})
#
# def reverse(reguest):
#     old_text = reguest.GET['usertext']
#     counter_words = len(old_text.split(''))
#     new_text = old_text[::-1]
#     print(reguest.GET)
#     return render(reguest,
#                   'reverse.html',
#                   {'rtv_texst': new_text})

def previw(request):
    return render(request, 'previw.html')