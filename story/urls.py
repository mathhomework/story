from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'story.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'creation.views.home', name='home'),
    url(r'^profile/', 'creation.views.profile', name='profile'),
    url(r'register/', 'creation.views.register', name='register'),
    url(r'^branches/', 'creation.views.show_branches', name='show_branches'),
)
