from django.conf import settings
from django.db import models

#from django.core.urlresolvers import reverse
from django_hosts.resolvers import reverse
from .utils import code_generator,create_shortcode
from .validators import validate_url,validate_dot_com


# Create your models here.

SHORTCODE_MAX=getattr(settings,"SHORTCODE_MAX",10)
#SHORTCODE_MAX=settings.SHORTCODE_MAX	Only if you don't want to reuse this code

class fesURLManager(models.Manager):
	def all(self,*args,**kwargs):
		qs_main=super(fesURLManager,self).all(*args,**kwargs)
		qs=qs_main.filter(active=True)
		return qs

	def refresh_shortcodes(self):
		qs=fesURL.objects.filter(id__gte=1)
		if items is not None and isinstance(items, int):
			qs = qs.order_by('-id')[:items]
		new_codes=0;
		for q in qs:
			q.shortcode=create_shortcode(q)
			q.save()
			new_codes+=1;
		return "New codes made: {i}".format(i=new_codes)

class fesURL(models.Model):
	url 		= models.CharField(max_length=220,validators=[validate_url,validate_dot_com])
	shortcode	= models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
	timestamp	= models.DateTimeField(auto_now_add=True)
	active		= models.BooleanField(default=True)

	
	objects=fesURLManager()			# Linking
	
	def save(self, *args, **kwargs):		#whenever you save, it automatically generates shortcode
		if self.shortcode is None or self.shortcode=="":		#if we leave it blank, it'd automatically fill it
			self.shortcode=create_shortcode(self)
		super(fesURL,self).save(*args,**kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)

	def get_short_url(self):
		url_path = reverse("scode", kwargs={'shortcode': self.shortcode}, host='www', scheme='http')
		return url_path

