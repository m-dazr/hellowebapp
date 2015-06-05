from django.shortcuts import render
from collection.models import Post

# Create your views here.
def index(request):
   # this is your new view
   posts = Post.objects.all()
   return render(request, 'index.html', {'posts': posts,})

def post_detail(request, slug):

	#grab object
	post = Post.objects.get(slug=slug)

	#pass to template
	return render(request, 'posts/post_detail.html', {'post': post,})


