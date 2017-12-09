from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    #host(r'blog', 'abcd.hostsconf.urls', name='blog'),
    host(r'(?!www).*', 'fes.hostsconf.urls', name='wildcard'),
)

# from abcd.hostsconf import urls as redirect_urls
# host_patterns=[
# 	host(r'www', settings.ROOT_URLCONF, name='www'),
#     #host(r'blog', 'abcd.hostsconf.urls', name='blog'),
#     host(r'(?!www).*', redirect_urls, name='wildcard'),
# ]