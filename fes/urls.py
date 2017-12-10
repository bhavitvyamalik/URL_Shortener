from django.conf.urls import url
from django.contrib import admin

from shortener.views import URLRedirectView,HomeView

# DO NOT DO
# from shortener import views
# from anotherApp import views

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^$',HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$',URLRedirectView.as_view(),name='scode'), 	#for class based view (see the difference)	
    
    #https://github.com/codingforentrepreneurs/Guides/blob/master/all/common_url_regex.md
    
    # DO NOT DO
	# url(r'^abc/$',shortener.views.fes_redirect_view),
	# url(r'^abc/$',views.fes_redirect_view()),

]
