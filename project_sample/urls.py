from django.views.generic import TemplateView
from django.conf.urls import include, url

from django.contrib import admin
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url


admin.autodiscover()

urlpatterns = [
    path('', include('main.urls')),
    #url(r'^$', TemplateView.as_view(template_name="homepage.html"),),
    url(r'^schedule/', include('schedule.urls')),
    url(r'^fullcalendar/', TemplateView.as_view(template_name="fullcalendar.html"), name='fullcalendar'),
    url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    #path('', include('main.urls')),
    re_path(r'^registration/logout/$', LogoutView.as_view(template_name='registration/logout.html'),
            name="logout"),
    re_path(r'^registration/login/$', LoginView.as_view(template_name='registration/login.html'), name="login"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
