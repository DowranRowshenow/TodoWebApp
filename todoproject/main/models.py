from django.conf import settings
from django.utils import timezone
from django.db import models

class Todo(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField(max_length=255, null=True, blank=True)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	is_favorite = models.BooleanField(default=False)
	is_completed = models.BooleanField(default=False)
	is_deleted = models.BooleanField(default=False)
	created_date_time = models.DateTimeField(default = timezone.now())
	target_date_time = models.DateTimeField(default = timezone.now())