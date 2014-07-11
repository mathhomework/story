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
    url(r'^register/', 'creation.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^user/logout/$', 'django.contrib.auth.views.logout', name='user_logout'),
    url(r'^stories/$', 'creation.views.stories', name='stories'),
    url(r'^stories/(?P<branch_id>\w+)/$', 'creation.views.view_branch', name='view_branch'),

)
