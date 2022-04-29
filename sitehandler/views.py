from django.shortcuts import render, redirect
from .models import *
from discord_webhook import DiscordWebhook
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.core.files.storage import FileSystemStorage


# Create your views here.
def homepage(request):
	if request.method == 'POST':
		name = request.POST['name']
		phno = request.POST['phno']
		mode = request.POST['mode']
		message = request.POST['message']
		contactus.objects.create(name=name,phno=phno,mode=mode,message=message)
		url_contact = "https://discord.com/api/webhooks/961563317296594994/RRggnxJb0OyfUS0pEqWfatbONuxtFbOyW6rQSBay2or8XKAAQEnSM_7ENI_9GmNOWMjT"
		content = "Name:\t"+name+"\nPhone Number:\t"+phno+"\nMode:\t"+mode+"\nMessage:\t"+message
		webhook = DiscordWebhook(url=url_contact, content=content)
		response = webhook.execute()
		print("Successfully inserted...")

	return render(request,'index.html')


def acservicebooking(request):
	if request.method == 'POST':
		name = request.POST['name']
		phno = request.POST['phno']
		address = request.POST['address']
		city = request.POST['city']
		pincode = request.POST['pincode']
		dos = request.POST['dos']
		purpose = request.POST['purpose']
		flag = "pending"
		ac_service_booking.objects.create(name=name,phno=phno,address=address,city=city,pincode=pincode,dos=dos,purpose=purpose,flag=flag)
		url_ac_services ="https://discord.com/api/webhooks/961211754082344990/YKqRWj_yWzkBdlRW8fxVAi6IS_IgMlsCj6lICYiDYelBh1NQvdtZADkWx_zTBCuHOkn8"
		content = "Name:\t"+name+"\nPhone Number\t"+phno+"\nAddress:\t"+address+"\nCity:\t"+city+"\nPincode:\t"+pincode+"\nDate of Service:\t"+dos+"\nPurpose:\t"+purpose+"\nStatus:\t"+flag
		webhook = DiscordWebhook(url=url_ac_services, content=content)
		response = webhook.execute()
		print("Successfully inserted.....")
	return render(request,'AC_service_booking.html')


def skater_registration(request):

	if request.method == 'POST':
		name = request.POST['name']
		phno = request.POST['phno']
		dob = request.POST['dob']
		fname = request.POST['fname']
		address = request.POST['address']
		aadhaar = request.POST['aadhaar']
		doj = request.POST['doj']
		branch = request.POST['branch']
		outsider = 'True'

		skater_registrations.objects.create(name=name,phno=phno,dob=dob,fname=fname,address=address,aadhaar=aadhaar,doj=doj,branch=branch,outsider=outsider)
		messages.success(request,("Registration Successfull!!!"))
		url_skating_reg ="https://discord.com/api/webhooks/961211299327528970/0OaO6_eCx9ACrqSOEU4hCf3527jqN8AHwHMYOLERpk85qEoHdugJXEqAtixI7yrZSsLN"
		content = "Name:\t"+name+"\nPhone Number\t"+phno+"\nDate of Birth:\t"+dob+"\nFather Name:\t"+fname+"\nAddress:\t"+address+"\nAadhaar:\t"+aadhaar+"\nDate of Joining:\t"+doj+"\nBranch:\t"+branch+"\nOutsider:"+outsider
		webhook = DiscordWebhook(url=url_skating_reg, content=content)
		response = webhook.execute()

	else:
		messages.success(request,("Please register your skater..."))
	
	return render(request,'skater_registration.html')


def dancer_registration(request):

	if request.method == 'POST':
		name = request.POST['name']
		phno = request.POST['phno']
		dob = request.POST['dob']
		fname = request.POST['fname']
		address = request.POST['address']
		aadhaar = request.POST['aadhaar']
		doj = request.POST['doj']
		branch = request.POST['branch']
		outsider = 'True'

		dancer_registrations.objects.create(name=name,phno=phno,dob=dob,fname=fname,address=address,aadhaar=aadhaar,doj=doj,branch=branch,outsider=outsider)
		messages.success(request,("Registration Successfull!!!"))
		url_dance_reg ="https://discord.com/api/webhooks/961914480768479253/54bV8blK5PoKY_bxQ0tccJlmMq0IurMZbzLq06IJt_TRAD_qpzBcFQKCxr3TnO8Kmvkk"
		content = "Name:\t"+name+"\nPhone Number\t"+phno+"\nDate of Birth:\t"+dob+"\nFather Name:\t"+fname+"\nAddress:\t"+address+"\nAadhaar:\t"+aadhaar+"\nDate of Joining:\t"+doj+"\nBranch:\t"+branch+"\nOutsider:"+outsider
		webhook = DiscordWebhook(url=url_dance_reg, content=content)
		response = webhook.execute()

	else:
		messages.success(request,("Please register your Dancer..."))
	return render(request,'dancer_registration.html')


def skating_coach_login(request):
	return render(request,'skating_coach_login.html')

def dance_choreographer_login(request):
	return render(request,'dance_choreographer_login.html')

def ac_service_login(request):
	return render(request,'ac_service_login.html')


def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		try:
			if user is not None:
				if user.is_staff:
					login(request, user)
					return redirect('adminhome')
				elif user.is_active:
					login(request,user)
					g = request.user.groups.all()[0].name
					print(g)
					if g == 'Skating_coach':
						return redirect('skating_coach_login')
					elif g == 'choreographer':
						return redirect('dance_choreographer_login')
					elif g == 'AC_service':
						return redirect('ac_service_login')

				else:
					messages.success(request,("There was an error logging in, Try Again!!"))
					return render(request,'login.html')
		except Exception as e:
			raise e
		

	return render(request, 'login.html', {})


def logout_user(request):
	if request.user.is_staff:
		logout(request)
		messages.success(request,("You were Logged out!"))
		return redirect('login_user')

	elif request.user.is_active:
		logout(request)
		messages.success(request,("You were Logged out!"))
		return redirect('login_user')

	else:
		return redirect('login_user')

def adminhome(request):
	if request.user.is_staff:
		return render(request,'admin_login.html')
	else:
		messages.success(request,("Please log into your account..."))
		return redirect('login_user')


def admin_skaters_outsiders(request):
	if request.user.is_staff:
		outside_skater = skater_registrations.objects.filter(outsider='True')
		return render(request,'admin_skaters_outsiders.html',{'outside_skater':outside_skater})

def skating_coach_outsiders(request):
	if request.user.is_active:
		g = request.user.groups.all()[0].name
		if g == 'Skating_coach':
			outside_skater = skater_registrations.objects.filter(outsider='True')
		return render(request,'skating_coach_outsiders_data.html',{'outside_skater':outside_skater})

def skating_coach_insiders(request):
	if request.user.is_active:
		g = request.user.groups.all()[0].name
		if g == 'Skating_coach':
			inside_skater = skater_registrations.objects.filter(outsider='False')
		return render(request,'skating_coach_insiders_data.html',{'inside_skater':inside_skater})

def dance_choreographer_insiders(request):
	if request.user.is_active:
		g = request.user.groups.all()[0].name
		if g == 'choreographer':
			inside_dancer = dancer_registrations.objects.filter(outsider='False')
		return render(request,'dance_choreographer_insiders_data.html',{'inside_dancer':inside_dancer})


def dance_choreographer_outsiders(request):
	if request.user.is_active:
		g = request.user.groups.all()[0].name
		if g == 'choreographer':
			outside_dancer = dancer_registrations.objects.filter(outsider='True')
		return render(request,'dance_choreographer_outsiders_data.html',{'outside_dancer':outside_dancer})

def ac_service_pending(request):
	if request.user.is_active:
		g = request.user.groups.all()[0].name
		if g == 'AC_service':
			pending_service = ac_service_booking.objects.filter(flag='pending')

		return render(request,'ac_service_pending.html',{'pending_service':pending_service})

def ac_service_done(request):
	if request.user.is_active:
		g = request.user.groups.all()[0].name
		if g == 'AC_service':
			done_service = ac_service_booking.objects.filter(flag='done')

		return render(request,'ac_service_completed.html',{'done_service':done_service})


def skating_coach_sendto_insider(request,pid):
	if not request.user.is_active:
		return redirect('login_user')

	skater_registrations.objects.filter(id=pid).update(outsider='False')
	return redirect('skating_coach_outsiders')

def skating_coach_sendto_outsider(request,pid):
	if not request.user.is_active:
		return redirect('login_user')

	skater_registrations.objects.filter(id=pid).update(outsider='True')
	return redirect('skating_coach_insiders')


def dance_choreographer_sendto_insider(request,pid):
	if not request.user.is_active:
		return redirect('login_user')

	dancer_registrations.objects.filter(id=pid).update(outsider='False')
	return redirect('dance_choreographer_outsiders')

def dance_choreographer_sendto_outsider(request,pid):
	if not request.user.is_active:
		return redirect('login_user')

	dancer_registrations.objects.filter(id=pid).update(outsider='True')
	return redirect('dance_choreographer_insiders')

def ac_service_sendto_done(request,pid):
	if not request.user.is_active:
		return redirect('login_user')

	ac_service_booking.objects.filter(id=pid).update(flag='done')
	return redirect('ac_service_done')

def ac_service_sendto_pending(request,pid):
	if not request.user.is_active:
		return redirect('login_user')

	ac_service_booking.objects.filter(id=pid).update(flag='pending')
	return redirect('ac_service_pending')


def skating_coach_delete(request,pid):
	if not request.user.is_active:
		return redirect('login_user')

	skater = skater_registrations.objects.get(id=pid)
	skater.delete()
	return redirect('skating_coach_insiders')

def dance_choreographer_delete(request,pid):
	if not request.user.is_active:
		return redirect('login_user')

	dancer = dancer_registrations.objects.get(id=pid)
	dancer.delete()
	return redirect('dance_choreographer_insiders')

def ac_service_delete(request,pid):
	if not request.user.is_active:
		return redirect('login_user')

	ac_service = ac_service_booking.objects.get(id=pid)
	ac_service.delete()
	return redirect('ac_service_pending')

def admin_skaters_insiders(request):
	if request.user.is_staff:
		inside_skater = skater_registrations.objects.filter(outsider='False')
		return render(request,'admin_skaters_insiders.html',{'inside_skater':inside_skater})


def admin_dancer_insiders(request):
	if request.user.is_staff:
		inside_dancer = dancer_registrations.objects.filter(outsider='False')
		return render(request,'admin_dancer_insiders.html',{'inside_dancer':inside_dancer})


def admin_dancer_outsiders(request):
	if request.user.is_staff:
		outside_dancer = dancer_registrations.objects.filter(outsider='True')
		return render(request,'admin_dancer_outsiders.html',{'outside_dancer':outside_dancer})

def admin_ac_services(request):
	if request.user.is_staff:
		acservices = ac_service_booking.objects.all()
		return render(request,'admin_ac_services.html',{'acservices':acservices})


