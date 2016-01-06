from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from models import *
# Create your views here.
def streamer(request):
	return HttpResponse(get_template('index.html').render())

def get_songs_list(request):
	songs_list = []
	for track in Song.objects.all():
		t = {"name":str(track.name), "url":str(track.url)}
		songs_list.append(t)
	return HttpResponse(str(songs_list).replace("'",'"'))

def add_song(request):
	if request.method == "POST":
		track = Song()
		track.name = request.POST["name"]
		track.url = request.POST["url"]
		track.save()
		return HttpResponse("Success")
	return HttpResponse("Failed")

