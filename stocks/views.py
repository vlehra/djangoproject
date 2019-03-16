from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.forms import  RawStockForm
from .models import Stock

# Create your views here.


@login_required

def stocks(request):

	stock = Stock.objects

	return render(request, 'stocks/stock.html', {'stock': stock})

def add_stocks(request):
	form = RawStockForm()
	if request.method == 'POST':
		form = RawStockForm(request.POST)
		if form.is_valid():
			
			print(form.cleaned_data)
			Stock.objects.create(**form.cleaned_data)
			return redirect('stocks')
		else:
			print(form.errors)

	context = {
	    'form': form
	}
	return render(request, 'stocks/add_stock.html', context)


def delete_stock(request, id):
	obj= get_object_or_404(Stock, id= id)
	if request.method == "POST":
		obj.delete()
		return redirect('stocks')
	context = {
        "object": obj
	}
	return render(request, 'delete_stock.html', context)