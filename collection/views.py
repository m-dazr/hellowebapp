from django.shortcuts import render

# Create your views here.
def index(request):
   # this is your new view
   number = 6
   return render(request, 'index.html', {'number': number,})