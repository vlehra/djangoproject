from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.forms import RawCustomerForm, RawCustomer1Form
from .models import Customer,Customer_detail
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import View 
from .utils import render_to_pdf
from django.template.loader import get_template
from math import ceil
# Create your views here.
@login_required	
def add_customers(request):
	if request.method == 'POST':
		form = RawCustomerForm(request.POST)
	
		if form.is_valid():
			form.save()
			context = { 'form': form,'error':' registration is complete !!' }

			return render(request, "customer/add_customers.html", context)
				
		else:
			context = { 'form': form,'error':' registration is not complete !!' }

			return render(request, "customer/add_customers.html", context)
	form = RawCustomerForm()
	context = {
	    
	    'form': form,
	    
	    
	   	
	}
	return render(request, 'customer/add_customers.html', context)



def get(request, id, *args, **kwargs):
		
		template = get_template('invoice.html')
		obj= get_object_or_404(Customer, id= id)
		context = {
		    'objects': obj
		}
		html = template.render(context)
		pdf = render_to_pdf('invoice.html', context)
		if pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			filename = "Invoice_%s.pdf" % id 
			content = "inline; filename='%s'" %(filename)
			download = request.GET.get("download")
			if download:
				content = "attachment; filename='%s'" %(filename)
			response['Content-Disposition'] = content
			return response
		return HttpResponse("Not Found")

def get_bill(request, id, *args, **kwargs):
		
		template = get_template('bill_invoice.html')
		obj= get_object_or_404(Customer_detail, id= id)
		
		context = {
		    'objects': obj,
		    
		}
		html = template.render(context)
		pdf = render_to_pdf('bill_invoice.html', context)
		if pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			filename = "Invoice_%s.pdf" % id 
			content = "inline; filename='%s'" %(filename)
			download = request.GET.get("download")
			if download:
				content = "attachment; filename='%s'" %(filename)
			response['Content-Disposition'] = content
			return response
		return HttpResponse("Not Found")











@login_required	

def customers(request):
	
	if request.method== 'POST':

		srch = request.POST['srh']

		if srch:
			match = Customer.objects.filter(Q(mobile_number__iexact=srch)|
				                            Q(date_cust__icontains=srch)|
				                            Q(name__icontains=srch)

				                            )

		#	match1 = Customername.objects.filter(Q(name__icontains=srch))
				                            


				                            


			if match: #and match1:
				context = {
					'sr':match,
		#			'sr1':match1,
				}



				return render(request, 'customer/customers.html', context)
			
			else:
				#messages.error(request, 'no result found.')
				return redirect('add_customers')
		else:
			return redirect('customers')

		return render(request, 'customer/customers.html')
	
	else:
		cust = Customer.objects.all()
		#cust1 = Customername.objects.all()
		context = {
			'cust':cust,
			#'cust1':cust1,
		}
		return render(request, 'customer/customers.html', context)





def dynamic_customers(request, id):
	obj = get_object_or_404(Customer, id= id)
	ob = Customer_detail.objects.all()
	
	

	
	if request.method == 'POST':
		
		form =RawCustomer1Form(request.POST)
		if form.is_valid():
			try:
				
				user = Customer.objects.get(mobile_number=request.POST['mobile_number'])
				form.save()
				
				context = { "object": obj, "ob":ob,}
				return redirect(obj)
			except Customer.DoesNotExist:
				context = { 'form': form,"object": obj, "ob":ob,'error':'No Mobile Number found !!' }

				return render(request, "customer/customers_details.html", context)
		else:
			print(form.errors)
	
	form = RawCustomer1Form()
	context = {
	    'form': form,
	    "object": obj,
	    "ob":ob,
	    
	   	
	}
	return render(request, 'customer/customers_details.html', context)



def delete_customer_detail(request, id):
	obj= get_object_or_404(Customer_detail, id= id)
	if request.method == "POST":
		obj.delete()

		return redirect('customers')
	context = {
        "obj": obj
	}
	return render(request, 'delete_customer_detail.html', context)



def delete_customer(request, id):
	obj= get_object_or_404(Customer, id= id)
	if request.method == "POST":
		obj.delete()

		return redirect('customers')
	context = {
        "obj": obj
	}
	return render(request, 'delete_customer_detail.html', context)