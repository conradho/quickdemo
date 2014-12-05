from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_tables2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'sample_datas.views.home'),
    url(r'^success/$', 'sample_datas.views.view_afterwards'),

)
