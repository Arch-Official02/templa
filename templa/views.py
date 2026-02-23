from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'templa/index.html')
def index(request):
	return render(request, 'templa/index.html')
def about(request):
	return render(request, 'templa/about.html')
def blog(request):
	return render(request, 'templa/blog.html')
def grid(request):
	return render(request, 'templa/grid.html')
def masonry(request):
	return render(request, 'templa/masonry.html')
def single_post(request):
	return render(request, 'templa/single-post.html')