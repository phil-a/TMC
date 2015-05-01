from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.shortcuts import render
from forms import MyRegistrationForm
# Create your views here.

def home(request):
        return render(request, "home.html")

def story(request):
        return render(request, "story.html")

def login(request):
	c = {} 										#dictionary
	c.update(csrf(request)) 					#push csrf request object
	return render_to_response('login.html', c) #pass through to login.html template

def auth_view(request):
	username = request.POST.get('username', '') #gets info from form and gets username
	password = request.POST.get('password', '')	#gets password
	user = auth.authenticate(username=username, password=password) #checks and return userObject or none

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin') #
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	return render_to_response('loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
	return render_to_response('invalid.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

def register_user(request):
	if request.method == 'POST': 				#does request have method of POST
		form = MyRegistrationForm(request.POST)	#pass values through
		if form.is_valid(): 					#validate
			form.save()
			return HttpResponseRedirect('/accounts/register_success')

	args = {}
	args.update(csrf(request)) #cross-site request forgery
	args['form'] = MyRegistrationForm()
	return render_to_response('register.html', args)

def register_success(request):
	return render_to_response('register_success.html')	