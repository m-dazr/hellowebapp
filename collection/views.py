from django.shortcuts import render, render_to_response, redirect
from collection.models import Post
from collection.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

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


	#edit post view

def create_post(request):
	form_class=PostForm

	#if coming from a submitted form,do this
	if request.method == 'POST':

		#grab data from form and apply to form

		form=form_class(request.POST)
		if form.is_valid():
			#create instance but dont save yet
			post = form.save(commit = FALSE)

			#set additional details
			post.user = request.user
			post.slug = slugify(post.name)


			#save the object
			post.save()

			#redirect to our newly created post
			return redirect('post_detail', slug=post.slug)

		#otherwise just create form
		else:

			form = form_class()


		return render(request, 'posts/create_post.html', {
			'form': form,
			})




 
def edit_post(request, slug):
    # grab the object...
    post = Post.objects.get(slug=slug)

    # grab the current logged in user and make sure they're the owner of the thing
    user = request.user
    if post.user != user:
        raise Http404

    # set the form we're using...
    form_class = PostForm

    # if we're coming to this view from a submitted form,  
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=post)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('post_detail', slug=post.slug)

    # otherwise just create the form
    else:
        form = form_class(instance=thing)

    # and render the template
    return render_to_response('posts/edit_post.html', {
        'post': post,
        'form': form,
    }, context_instance=RequestContext(request))  

def browse_by_title(request, initial=None):
    
    if initial:
        posts = Post.objects.filter(
            title__istartswith=initial).order_by('title')
    else:
        posts = Post.objects.all().order_by('title')

    return render_to_response('search/search.html', {
        'posts': posts,
        'initial': initial,
    })