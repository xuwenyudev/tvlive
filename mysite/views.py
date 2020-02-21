from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from datetime import datetime

def index(request, tvno='0'):
	if(tvno != '0' and tvno != '1'):
		raise Http404('找不到指定的频道')
	tv_list = [{'name':'CCTV News', 'tvcode':'XNDU0Mjc0NjA0MA=='},
	{'name':'CCTV 中文国际', 'tvcode':'XNDU0Mjc0NjA0MA=='},]

	template = get_template('index.html')
	now = datetime.now()
	tvno = tvno
	tv = tv_list[int(tvno)]
	html = template.render(locals())
	return HttpResponse(html)

# Create your views here.
