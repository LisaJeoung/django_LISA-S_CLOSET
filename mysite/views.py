from django.shortcuts import render, get_object_or_404
from .models import MainContent


def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)


def aboutCompany(request):
    return render(request, 'mysite/aboutCompany.html')


def detail(request, content_id):
    content_list = get_object_or_404(MainContent, pk=content_id)
    context = {'content_list': content_list}
    return render(request, 'mysite/productDetail.html', context)


def mypage(request):
    return render(request, 'mysite/mypage.html')
