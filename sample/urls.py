from django.conf.urls import patterns, include, url
from django.contrib import admin
from login.views import IndexView

admin.autodiscover()

urlpatterns = patterns('',
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view()),
    url(r'^logout/$', 'login.views.log_out'),
    url(r'^deauthorize/$', 'login.views.deauthorize'),
)
