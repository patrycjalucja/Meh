from django.shortcuts import render
from .models import Trial
from django.utils import  timezone
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Trial.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'main/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Trial, pk=pk)
    return render(request, 'main/post_detail.html', {'post': post})
