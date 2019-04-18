from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.forms import ParticularForm, RawParticularForm
from .models import Menu


 

# Create your views here.

@login_required




def veg(request):

	products = Menu.objects

	return render(request, 'menu/veg.html', {'products': products})



def egg(request):

	products = Menu.objects

	return render(request, 'menu/egg.html', {'products': products})



def non_veg(request):

	products = Menu.objects

	return render(request, 'menu/non_veg.html', {'products': products})


def add_particulars(request):
	form = RawParticularForm()
	if request.method == 'POST':
		#if request.POST['serial'] and request.POST['item'] and request.POST['rate']:
			#form = ParticularForm(request.POST or None)
			#form.serial = request.POST['serial']
			#form.item = request.POST['item']
			#form.veg = request.POST['veg']
			#form.rate = request.POST['rate']
			#form.save()
			#context = {
			  #  'form': form
			#}
			#return render(request, 'add_particulars.html', context)
		#else:
			#return render(request, 'add_particulars.html', {'error':'please fill all the * required fields'})
	#else:
	#	return render(request, 'add_particulars.html' )
	    form = RawParticularForm(request.POST)
	    if form.is_valid():
		#form.save()

		     print(form.cleaned_data)
		     Menu.objects.create(**form.cleaned_data)
		     return redirect('particulars')
	    else:
		     print(form.errors)

	context = {
	    'form': form
	}
	return render(request, "menu/add_particulars.html", context)



def delete(request, id):
	obj= get_object_or_404(Menu, id= id)
	if request.method == "POST":
		obj.delete()
		return redirect('particulars')
	context = {
        "object": obj
	}
	return render(request, 'delete.html', context)


