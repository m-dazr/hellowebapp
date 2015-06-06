from django.shortcuts import render, redirect
from collection.models import Post
from collection.forms import PostForm

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


def edit_post(request, slug):
	#grab object
	post = Post.objects.get(slug=slug)
	#set the form used
	form_class = PostForm

	#if coming to this view from a submitted form

	if request.method == 'POST':
		#grab data from form and apply to form
		form = form_class(data=request.POST, instance=post)

		if form.is_valid():
		#save data
			form.save()
			return redirect('post_detail', slug=post.slug)

	#else just create form

	else:
		form = form_class(instance=post)

	#and render template
	return render(request, 'posts/edit_post.html', {'post': post, 'form': form, })