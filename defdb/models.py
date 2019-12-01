from django.db import models
from django.core.validators import EmailValidator 
from datetime import date
# Create your models here.
def default_country():
	return "India"

STATE_NAMES = (
				('T', 'Telangana'),
				('A', 'AndhraPradesh')
			  )	


class Customer(models.Model):
	cid = models.IntegerField()
	cname = models.CharField(max_length=20)
	cphno = models.CharField(max_length=10)
	cemail = models.CharField(max_length=20, validators=[EmailValidator])
	caddress = models.CharField(max_length=50)
	cstate = models.CharField(choices=STATE_NAMES,max_length=1)
	ccountry = models.CharField(max_length=30,default=default_country, help_text="""Ensure to provide your country""")
	date = models.DateField(default=date.today)
    # datetime = models.DateTimeField(default=timezone.now)
