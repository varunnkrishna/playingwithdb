from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
	list_display = ['cname', 'cphno', 'cemail', 'caddress','cstate']

	class meta:
		model = Customer

admin.site.register(Customer, CustomerAdmin)
