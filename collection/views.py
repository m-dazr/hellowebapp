from django.shortcuts import render
from collection.models import Post

# Create your views here.
def index(request):
   # this is your new view
   posts = Post.objects.all()
   return render(request, 'index.html', {'posts': posts,})