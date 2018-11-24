from django.shortcuts import render
from .models import Trial
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import GuestForm
from django.http import *

def post_list(request):
    posts = Trial.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'main/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Trial, pk=pk)
    return render(request, 'main/post_detail.html', {'post': post})


def send_email(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        print('poscik')
    else:
        form = GuestForm(request.GET)
        print('co innego')
    if form.is_valid():
        print('ok')
    return HttpResponse('dzieki, ' + form.cleaned_data[
        'name'] + '. Ta część jest jeszcze w budowie i potwierdzenie NIE zostało wysłane.')
