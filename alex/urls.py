from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'alex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^users/', include('users.urls', namespace = 'users')),
    url(r'^admin/', include(admin.site.urls)),
    
]
