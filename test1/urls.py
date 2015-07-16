from django.conf.urls import patterns, url, include
from django.views.generic import ListView, TemplateView
from test1.views import PostDetailView, login, logged_in, test11, entrypoint, entrypointdet
from test1.models import Post
from django.contrib import admin
#REMOVE#
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^blot/', ListView.as_view(
        queryset=Post.objects.all(),
        context_object_name="posts_list"),
        name="home"
    ),
    url(r'^post/(?P<slug>[a-zA-Z0-9-]+)/$', PostDetailView.as_view(
        queryset=Post.objects.all(),
        context_object_name="post"),
        name="post"
    ),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^login/$', login)
    url(r'^login/$', 'django.contrib.auth.views.login'),
    #url(r'^login/$', my_view),
    url(r'^welcome/$', logged_in),
    url(r'^welcome/home/$', entrypoint),
    url(r'^testo/$', test11),
    #
    url(r'^entry/(?P<slug>[a-zA-Z0-9-]+)/$', entrypointdet, name="entry"),
    #
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    #url(r'^AdminLTE/logged_in.html', my_view)
    #url(r'^mainsite/', TemplateView.as_view(template_name="AdminLTE/index.html"), name='menu')
)
#REMOVE#
#urlpatterns += staticfiles_urlpatterns()