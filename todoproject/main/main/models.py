from django.db import models
import datetime
from django.contrib.auth.models import User

class Todo(models.Model):
	content = models.TextField()
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	is_favorite = models.BooleanField(default=False)
	is_deleted = models.BooleanField(default=False)
	is_completed = models.BooleanField(default=False)
	created_at_server_time = models.DateTimeField(default = datetime.datetime.now())
	target_date = models.DateField(default = datetime.datetime.now())