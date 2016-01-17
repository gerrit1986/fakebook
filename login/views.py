from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

def log_out(request):
    logout(request)
    return redirect('/')
