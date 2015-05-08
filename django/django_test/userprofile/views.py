from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import UserProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.

#login confirmation code built in
@login_required
def user_profile(request):
	if request.method == 'POST':
		#prepopulates
		form = UserProfileForm(request.POST, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/loggedin')

	else:
		user = request.user
		profile = user.profile #triggers getorcreate
		form = UserProfileForm(instance=profile)

	#add csrf, form, and render
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('profile.html', args)	
