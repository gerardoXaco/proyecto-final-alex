from django.shortcuts import render, redirect

# Create your views here.
def foro(request):
	return render(request,'foro.html')
