from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent

from .models import fesURL
from .forms import SubmitUrlForm

# Create your views here.

class HomeView(View):
	def get(self,request,*args,**kwargs):
		the_form=SubmitUrlForm()
		context= {
			"title": "FES.co",
			"form": the_form,
		}
		return render(request,"shortener/home.html",context)		#by default django looks within the apps for template

	def post(self,request,*args,**kwargs):
		form=SubmitUrlForm(request.POST)
		context= {
			"title": "FES.co",
			"form": form,
		}
		template="shortener/home.html"
		if form.is_valid():
			new_url=form.cleaned_data.get("url")
			obj,created=fesURL.objects.get_or_create(url=new_url)
			context= {
				"object":obj,
				"created":created,	
			}
			if created:
				template="shortener/success.html"
			else:
				template="shortener/already_exists.html"

		return render(request,template,context)


class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = fesURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)

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