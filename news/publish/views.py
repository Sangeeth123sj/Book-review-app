

#from django.template.context_processors import csrf
from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect

import datetime

from .models import Book 
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout

#from django.middleware.csrf import get_token

# Create your views here.
def index(request):
	
    return HttpResponse("Hello worldwe")

	
def edit(request):
	if request.method=='POST':
		book = request.POST['book']
		name = request.POST['name']
		description = request.POST['detail']
		return render(request, 'edit.html', {'book':book, 'book_name':name, 'book_description':description})

def edit_save(request):
	id = request.POST['book_id']
	name = request.POST['name']
	detail = request.POST['detail']
	p = Book.objects.filter(id=id)
	r= Book.objects.get(id=id)
	r.book_name=name
	r.description=detail
	r.save()
	return HttpResponse("Book edited")


def delete(request):

	id= request.POST['book']
	p = Book.objects.filter(id=id)
	r= Book.objects.get(id=id)
	p.delete()
	return render(request, 'delete_status.html', {'deleted_book':r, 'book_id':id})


def current_datetime(request):
	now = datetime.datetime.now()
	book_list = Book.objects.all()
	#book_pic = Book.objects.image()
	return render(request, 'current_datetime.html', {'current_date': now, 'books':book_list})

def timeahead(request, offset):
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	
	return render(request,'future_time.html',{'future_time':dt, 'added_hours':offset})

def search_form(request):
	return render(request, 'search_form.html')

def search(request):
		message = 'You searched for: %r' % request.GET['q']
		q = request.GET['q']
		books = Book.objects.filter(book_name__icontains=q)
		return render(request, 'search_result.html', {'books': books, 'query': q})
	#else:
	#	message = 'You submitted an empty form.'
	#return HttpResponse(message)

def register(request):


	return render(request, 'register.html')

def submit(request):
	
		name = request.POST['name']
		detail=request.POST['detail']
		pic = request.FILES['image']
		
		p = Book(book_name=name, description=detail, image=pic, )
		p.save()
		
		#pic_obj = Book.objects.get(image=)
		return render(request, 'add_status.html', {'name':name,'detail':detail})
	





def loginpage(request):
  
  return render(request,'login.html')

def login(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username=username,password=password)
	if user is not None:
		if user.is_active:
			return HttpResponseRedirect('/dater/')
			# success page
		else:
			return HttpResponse("disabled account")
	else:
		return HttpResponse('Invalid login')


def logout(request):
	logout(request)
	return HttpResponse('Logout success')

def contact(request):

	if request.method == 'POST':
		#generate form data with POSTed data
		form = contactForm(request.POST)
		#check if valid
		if form.is_valid():
			#process data, insert into db, send mail,etc
			#redirect:
			return HttpResponse('thank you')

	else:
		# GET, generate blank form:
		form = contactForm()
		return render(request, 'form.html', {'form':form})

	return render(request, 'form.html', {'form':form})

def picture(request):
	if request.method == 'POST':
		form = Picture_Form(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return HttpResponse('Upload Success')
	else:
		form = Picture_Form()
	return render(request, 'test.html', {'form': form})

def picture_status(request):
	pics = Picture.objects.all()
	return render(request, 'display_pictures.html', {'pics':pics})


def signup(request):
	
	if request.method == 'GET':
		return render(request, 'signup_details.html')
	else :
		name = request.POST['username']
		password = request.POST['password']
		new_signup = User.objects.create_user(name,'sangeeth123sj@gmail.com',password)
		new_signup.save()
		return render(request, 'signup_status2.html')