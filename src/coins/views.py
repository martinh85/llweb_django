from django.shortcuts import render
from django.http import HttpResponse
from .models import Coin

from static.inputs import coins_list


def base(request):
	context = {
		"coins_list": coins_list
	}
	return render(request, 'base.html', context)


def home(request):
	return render(request, 'home.html')
