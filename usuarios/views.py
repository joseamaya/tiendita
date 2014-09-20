from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from usuarios.forms import SignUpForm

# Create your views here.
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			user = User.objects.create_user(username, email, password)
			user.first_name = first_name
			user.last_name = last_name

			user.save()
			return HttpResponseRedirect(reverse('usuarios:signup'))
	else:
		form = SignUpForm()
	context = {'form':form,}
	return render(request, 'signup.html', context)
