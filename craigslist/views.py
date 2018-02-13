from django.shortcuts import render
from scrapy_app import emails
import os
from craigslist.utils import start_urls_maker

def index(request):
	return render(request, "home.html")

def action(request):
	model = request.POST.get("model")
	email = request.POST.get("email")
	urls = start_urls_maker(model)
	# os.system("cd.. & cd scrappy_app & dir")
	os.system("cd scrapy_app & del cars.csv & scrapy crawl cars -o cars.csv -t csv -a model={0}".format(model))
	os.system("cd scrapy_app & python emails.py %s" % email)
	return render(request, "success.html")