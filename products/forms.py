from django import forms
from .models import Menu
from stocks.models import Stock
from frame.models import Feedback
from customers.models import Customer, Customer_detail
from phonenumber_field.formfields import PhoneNumberField


class ParticularForm(forms.ModelForm):
	class Meta:
		model = Menu
		fields = [
		    #'serial',
		    'item',
		    'rate'
		] 



class RawParticularForm(forms.Form):
	#serial = forms.CharField(label='serial')
	item = forms.CharField(label='items', widget=forms.TextInput(attrs={"placeholder": "Your Dish"}))
	description = forms.CharField(
		                required=False,
		                widget=forms.Textarea(
		                	    attrs={
		                	         "placeholder":"Your description",
		                	         "rows": 10,
		                	         "cols": 60
		                	    }

		                	)
		                )
	
	rate = forms.DecimalField()
	veg  = forms.BooleanField(required=False, initial=False, label='veg')
	egg  = forms.BooleanField(required=False, initial=False, label='egg')
	non_veg  = forms.BooleanField(required=False, initial=False, label='non veg')

		




class RawStockForm(forms.Form):
	#serial = forms.CharField(label='serial')
	item = forms.CharField(label='items', widget=forms.TextInput(attrs={"placeholder": "Your item"}))
	summary = forms.CharField(
		                required=False,
		                widget=forms.Textarea(
		                	    attrs={
		                	         "placeholder":"Your summary",
		                	         "rows": 10,
		                	         "cols": 60
		                	    }

		                	)
		                )
	
	
	qty = forms.DecimalField()
	rate = forms.DecimalField()
	

class RawCustomerForm(forms.ModelForm):
	class Meta:
		model =  Customer
		fields = ('name','mobile_number','male','female','address','gym','summary', 'order','qty','amount_paid')
	
	def __init__(self,  *args, **kwargs):
		super(RawCustomerForm, self).__init__(*args, **kwargs)
		self.fields['order'].widget = forms.CheckboxSelectMultiple()


class RawCustomer1Form(forms.ModelForm):
	class Meta:
		model =  Customer_detail
		fields = ('mobile_number', 'particular','qty','amount_paid')
	def __init__(self,  *args, **kwargs):
		super(RawCustomer1Form, self).__init__(*args, **kwargs)
		self.fields['particular'].widget = forms.CheckboxSelectMultiple()
	

	
class RawFeedbackForm(forms.ModelForm):
	class Meta:
		model =  Feedback
		fields = ('name','mobile_number','suggestions')

	def __init__(self,  *args, **kwargs):
		super(RawFeedbackForm, self).__init__(*args, **kwargs)
		self.fields['suggestions'].widget = forms.Textarea(
		                	    attrs={
		                	         "placeholder":"Your Suggestion",
		                	         "rows": 10,
		                	         "cols": 60
		                	    }

		                	)
		                