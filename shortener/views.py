from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import fesURL
# Create your views here.

def test_view(request):
	return HttpResponse("some stuff")

def fes_redirect_view(request,shortcode=None,*args,**kwargs):	
	obj=get_object_or_404(fesURL,shortcode=shortcode)
	return HttpResponseRedirect(obj.url)


class fesCBView(View):	#Class Based View
	def get(self,request,shortcode=None,*args,**kwargs):
		#print(shortcode)
		obj=get_object_or_404(fesURL,shortcode=shortcode)
		return HttpResponseRedirect(obj.url)

	def post(self,request,*args,**kwargs):
		return HttpResponse()


'''
def fes_redirect_view(request,shortcode=None,*args,**kwargs):
	#print(shortcode)
	
	obj=get_object_or_404(fesURL,shortcode=shortcode)
	obj_url=obj.url
	# try:
	# 	obj=fesURL.objects.get(shortcode=shortcode)
	# except:
	# 	obj=fesURL.objects.all.first()	#first item in that query set

	# obj_url=None
	# qs=fesURL.objects.filter(shortcode__iexact=shortcode.upper())
	# if qs.exists() and qs.count()==1:
	# 	obj=qs.first()
	# 	obj_url=obj.url

	return HttpResponse("hello {sc}".format(sc=obj_url))

'''