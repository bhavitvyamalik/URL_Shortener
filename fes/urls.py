"""fes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from shortener.views import fes_redirect_view,fesCBView,test_view

# DO NOT DO
# from shortener import views
# from anotherApp import views

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^about123/$',test_view),
    url(r'^(?P<shortcode>[\w-]+){6,10}/$',fes_redirect_view),	#for function based view
    url(r'^b/(?P<shortcode>[\w-]+){6,10}/$',fesCBView.as_view()),	#for class based view (see the difference)	
    
    #https://github.com/codingforentrepreneurs/Guides/blob/master/all/common_url_regex.md
    
    # DO NOT DO
	# url(r'^abc/$',shortener.views.fes_redirect_view),
	# url(r'^abc/$',views.fes_redirect_view()),

]
