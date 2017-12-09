import random
import string

#from shortener.models import fesURL
from django.conf import settings

SHORTCODE_MIN=getattr(settings,"SHORTCODE_MIN",15)

def code_generator(size=SHORTCODE_MIN, chars='string.ascii_lowercase+string.digits'):
	new_code=''
	for _ in range(size):
		new_code+=random.choice(chars)
	return new_code


def create_shortcode(instance, size=SHORTCODE_MIN):	
	new_code=code_generator(size=size)		# make sure codeis unique
	Klass=instance.__class__				# getting class from instance
	qs_exists=Klass.objects.filter(shortcode=new_code).exists()
	if qs_exists:
		return create_shortcode(size=size)
	return new_code