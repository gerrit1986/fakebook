from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import TemplateView
from social.pipeline.social_auth import social_uid

class IndexView(TemplateView):
    # current_user = UserSocialAuth.objects.all()[0]
    # first_name = current_user.extra_data['first_name']
    # last_name = current_user.extra_data['last_name']
    uid = social_uid()
    template_name = 'index.html'

def log_out(request):
    logout(request)
    return redirect('/')
