from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
	return render(request,'resblog/home.html')

def index(request):
	content={
		'post':Post.objects.all()
	}
	return render(request,'resblog/index.html',content)

def about(request):
	return render(request,'resblog/about.html')

