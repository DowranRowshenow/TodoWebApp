from django.conf import settings
from django.utils import timezone
from django.db import models

class Todo(models.Model):
	content = models.TextField()
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	is_favorite = models.BooleanField(default=False)
	is_deleted = models.BooleanField(default=False)
	is_completed = models.BooleanField(default=False)
	created_date_time = models.DateTimeField(default = timezone.now())
	target_date = models.DateField(default = timezone.now())