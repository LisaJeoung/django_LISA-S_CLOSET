from django.shortcuts import render
from .models import MainContent


def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)


def aboutCompany(request):
    return render(request, 'mysite/aboutCompany.html')


def login(request):
    return render(request, 'mysite/login.html')


def signup(request):
    return render(request, 'mysite/signup.html')


def productDetail(request):
    return render(request, 'mysite/productDetail.html')

def mypage(request):
    return render(request, 'mysite/mypage.html')
