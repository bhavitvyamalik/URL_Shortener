from django import forms

from .validators import validate_url,validate_dot_com

class SubmitUrlForm(forms.Form):
	url=forms.CharField(label='',validators=[validate_url,validate_dot_com])

	# def clean(self):			#for form
	# 	cleaned_data=super(SubmitUrlForm,self).clean()
	# 	# url=cleaned_data['url']
	# 	# print(url)

	def clean_url(self):		#for individual field
		url=self.cleaned_data['url']
		#print(url)
		#url_validator=URLValidator()
		# try:
		# 	url_validator(url)
		# except:
		# 	raise forms.ValidationError("Invalid URL for this field")
		if "http" in url:
			return url
		return "http://"+url