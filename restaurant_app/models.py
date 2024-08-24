from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Table(models.Model):
	name = models.CharField(max_length=50, blank=False)
	location = models.CharField(max_length=150, blank=False)
	is_available = models.BooleanField(default=True)
	table_img = models.ImageField(blank=True, upload_to="cover/")

	def __str__(self):
		return str(self.name)

class Message(models.Model):
	name = models.CharField(max_length=50, blank=False)
	email = models.CharField(max_length=150, blank=False)
	message = models.TextField("Messages", blank=True)

	def __str__(self):
		return str(self.name)

class Status(models.Model):
	name = models.CharField(max_length=50, blank=False)

	class Meta:
		verbose_name_plural = 'Status'

	def __str__(self):
		return str(self.name)


class Booking(models.Model):
	name = models.CharField(max_length=50, blank=False)
	email = models.CharField(max_length=150, blank=False)
	contact = models.CharField(max_length=50, blank=True)
	guests = models.IntegerField(default=1, blank=True)
	date = models.DateField(auto_now_add=True)
	time = models.CharField(max_length=50, blank=False)
	message = models.TextField("Enquiry", blank=True)
	table = models.ForeignKey(Table, blank=True, on_delete=models.CASCADE)
	status = models.ForeignKey(Status, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.name)


class Profile(models.Model):
	user=models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
	profile_picture = models.ImageField(blank=True, upload_to="profile_pictures/")
	contact = models.CharField(blank=True, max_length=500)
	bookings = models.ManyToManyField(Booking, related_name='book', blank=True)
	selected_choice = models.CharField(blank=True, max_length=500)
	selected_reservation = models.CharField(max_length=300, blank=True)

	def __str__(self):
		return f'{self.user.username}'

def create_profile(sender, instance, created, **kwargs):
	if created:
		profile = Profile(user=instance)
		profile.save()

post_save.connect(create_profile, sender=User)

class Notification(models.Model):
	message = models.TextField("Message", blank=True)

	def __str__(self):
		return str(self.name)