from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$','engiapp.views.main_page'),
	(r'^login/$', 'django.contrib.auth.views.login'), 
        (r'^logout/$','engiapp.views.logout_page'), 
        (r'^register/$','engiapp.views.register_page'),
        (r'^committee/$','engiapp.views.all_committee'),
        (r'^committee/(?P<committee_id>\d+)/$','engiapp.views.committee'),
        (r'^events/$','engiapp.views.all_events'),
        (r'^events/(?P<event_id>\d+)/$' , 'engiapp.views.event'),

	(r'^register/success/$',TemplateView.as_view(template_name="registration/register_success.html")), 
    # Examples:
    # url(r'^$', 'engisite.views.home', name='home'),
    # url(r'^engisite/', include('engisite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
