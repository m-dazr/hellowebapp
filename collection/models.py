from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	slug = models.SlugField(unique=True)

	user = models.OneToOneField(User, blank=True, null=True)