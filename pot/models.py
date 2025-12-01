from django.db import models


class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	link = models.URLField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class FAQ(models.Model):
	question = models.CharField(max_length=255)
	answer = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.question


class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	subject = models.CharField(max_length=200, blank=True)
	message = models.TextField()
	BUDGET_CHOICES = [
		('', 'Not sure / Discuss'),
		('1k-5k', '$1k–$5k'),
		('5k-20k', '$5k–$20k'),
		('20k+', '$20k+'),
	]
	budget = models.CharField(max_length=20, choices=BUDGET_CHOICES, blank=True, default='')
	created_at = models.DateTimeField(auto_now_add=True)
	is_read = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.name} <{self.email}> - {self.subject or 'No subject'}"


class About(models.Model):
	name = models.CharField(max_length=100, default='Your Name')
	tagline = models.CharField(max_length=255, blank=True, default='Digital Creator & Problem Solver')
	bio = models.TextField(blank=True, default='Write your bio here. Include experience and mission.')
	skills = models.TextField(blank=True, default='Python\nDjango\nJavaScript\nUI/UX')
	github = models.URLField(blank=True, null=True)
	linkedin = models.URLField(blank=True, null=True)
	website = models.URLField(blank=True, null=True)

	class Meta:
		verbose_name = 'About'
		verbose_name_plural = 'About'

	def skills_list(self):
		return [s.strip() for s in self.skills.splitlines() if s.strip()]

	def __str__(self):
		return f"About: {self.name}"


class Post(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	excerpt = models.TextField(blank=True)
	content = models.TextField()
	published = models.BooleanField(default=True)
	published_at = models.DateTimeField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-published_at', '-created_at']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('pot:blog_detail', kwargs={'slug': self.slug})
