from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from products.forms import RawFeedbackForm
from .models import Feedback

@login_required
		
def home_view(request, *args, **kwargs):
	ob = Feedback.objects.all()
	if request.method == 'POST':
		
		form =RawFeedbackForm(request.POST)
		
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			print(form.errors)
	
	form = RawFeedbackForm()
	context = {
	    'form': form,
	    "ob":ob,
	    
	   	
	}
	return render(request, "home.html", context)
	