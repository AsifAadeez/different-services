from django.conf.urls import include, url
from django.contrib import admin
from demo.views import home,service



urlpatterns = [
			    url(r'^admin/', include(admin.site.urls)),
			    url(r'^$',home),
			    url(r'^category/(?P<id>[\w\-]+)/$',service),
			 ]