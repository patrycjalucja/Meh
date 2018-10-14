from django.urls import path, reverse
from main import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

]

"""
@ajax
def cos():
    c = 1 + 3
    print("cos dziala")
    return HttpResponse("hejjj")


cos()


class SimpleView(AJAXMixin, TemplateView):
    template_name = 'post_list.html'

"""
