from django.shortcuts import render,redirect 
from .forms import UserAdminCreationForm

def UserRegisterView(request):

	if request.POST:
		form = UserAdminCreationForm(request.POST)

		if form.is_valid():
			form.save()

			return redirect('index')
	else:

		form = UserAdminCreationForm()
	return render(request, 'Accounts/Register.html',{'form':form})



