from django.db import models

# Create your models here.
class contactus(models.Model):
	name = models.TextField()
	phno = models.TextField()
	mode = models.TextField()
	message = models.TextField()

	def __str__(self):
		return self.name

class ac_service_booking(models.Model):
	name = models.TextField()
	phno = models.CharField(max_length=10)
	address = models.TextField()
	city = models.CharField(max_length=30)
	pincode = models.CharField(max_length=10)
	dos = models.DateField()
	purpose = models.TextField()
	flag = models.CharField(max_length=8)

	def __str__(self):
		return self.name

class skater_registrations(models.Model):
	name = models.CharField(max_length=50)
	phno = models.CharField(max_length=10)
	dob = models.DateField()
	fname = models.CharField(max_length=50)
	address = models.TextField()
	aadhaar = models.CharField(max_length=12,unique=True)
	doj = models.DateField()
	branch = models.CharField(max_length=50)
	outsider = models.CharField(max_length=10)

	def __str__(self):
		return self.aadhaar

class dancer_registrations(models.Model):
	name = models.CharField(max_length=50)
	phno = models.CharField(max_length=10)
	dob = models.DateField()
	fname = models.CharField(max_length=50)
	address = models.TextField()
	aadhaar = models.CharField(max_length=12,unique=True)
	doj = models.DateField()
	branch = models.CharField(max_length=50)
	outsider = models.CharField(max_length=10)

	def __str__(self):
		return self.aadhaar

