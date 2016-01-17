from django.contrib.auth import logout
from django.shortcuts import redirect
from django.template import RequestContext
from django.views.generic import TemplateView
from social.apps.django_app.default.models import UserSocialAuth


class IndexView(TemplateView):
    template_name = 'index.html'

    def uid(self, request):
        request_context = RequestContext(request)
        # TODO: Check for user in RequestContext and use it to get his picture
        uid = UserSocialAuth.objects.all()[0].uid
        return uid

def log_out(request):
    logout(request)
    return redirect('/')

def deauthorize():
    # TODO: Implement this.
    pass
