from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from defdb.forms import CustomerForm

# Create your views here.
def index(request):
	return render(request, 'defdb/index.html')

def customersearch(request):
		if request.method == 'POST':
			search = request.POST['searchbar']

			if search:
				match = Customer.objects.filter(cname__icontains=search)

				if match:
					return render(request, 'defdb/customersearchresult.html', {'details': match } )
				else:
					return HttpResponse('no search results found')

			else:
				return HttpResponseRedirect('/')

		else:
			return render(request, 'defdb/index.html')


def customerinput(request):
	if request.method == 'POST':
		print('post sucess')
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			print('form saved')
			return HttpResponse('sucess')
	else:
		form = CustomerForm()
	return render(request, 'defdb/customerinput.html', {'form': form})


