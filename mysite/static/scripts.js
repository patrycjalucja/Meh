from django.views.generic import TemplateView, View
from django.http import HttpResponse

class HomeView(TemplateView):
    template_name = "post_list.html"

home = HomeView.as_view()


class AjaxView(View):
    def post(self, request, **kwargs):
        return HttpResponse('ok')

ajax_view = AjaxView.as_view()

$(document).ready(function(){
    $.ajax({
	url: configuration['main']['ajax_view'],
	cache: false,
	type: "POST",
	success: function(data){
	}
    });
});