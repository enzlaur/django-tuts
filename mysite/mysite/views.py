from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render


from django.http.response import Http404

def index(request):
    template = loader.get_template('index.html')
    page_render = template.render(request)
    return HttpResponse(page_render)
    # return render(request, 'mysite/index.html')