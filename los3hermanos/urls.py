from django.conf.urls import include, url
from django.contrib import admin
from core.views import HomeController

urlpatterns = [
    # Examples:
    # url(r'^$', 'los3hermanos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home', HomeController.as_view()),
]