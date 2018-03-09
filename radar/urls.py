from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login

import data.urls
import review.urls


urlpatterns = [
    url(r'^accounts/login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^accounts/logout/$', logout_then_login, name='logout'),
    url(r'^auth/', include('django_lti_login.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^', include(data.urls)),
    url(r'^', include(review.urls)),
]
