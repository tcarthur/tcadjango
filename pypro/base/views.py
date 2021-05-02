from http.client import HTTPResponse
from django.shortcuts import render # noqa

# Create your views here.


def home(request):
    return HTTPResponse('Olá Django')
