from django.shortcuts import render
from .models import Trial
from django.utils import  timezone

def post_list(request):
    posts = Trial.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'main/post_list.html', {'posts': posts})
