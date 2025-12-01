from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .models import Project, FAQ, About
from .models import Post
from .forms import ContactForm


def index(request):
	projects = Project.objects.all().order_by('-created_at')
	# Stats used in the home page — simple example values, adjust as required
	context = {
		'projects': projects,
		'featured_projects': projects[:6],
		'about': About.objects.first(),
		'projects_count': projects.count() or 0,
		'clients_satisfaction': '98%',
		'team_member_count': 50,
		'support_hours': '24/7',
	}
	return render(request, 'pot/home.html', context)


def about(request):
	about = About.objects.first()

	# Fallback values if nothing is configured in the admin
	context = {
		'about': about,
	}
	return render(request, 'pot/about.html', context)


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			contact = form.save()
			# Send an admin email notification — settings must define EMAIL_BACKEND or fallback
			try:
				from django.conf import settings
				from django.core.mail import send_mail
				subject = f"New contact: {contact.subject or 'No subject'}"
				message = f"From: {contact.name} <{contact.email}>\n\n{contact.message}"
				recipients = [a[1] for a in getattr(settings, 'ADMINS', [])]
				if not recipients:
					# fallback to DEFAULT_FROM_EMAIL if ADMINS is not configured
					recipients = [getattr(settings, 'DEFAULT_FROM_EMAIL', '')]
				# Only send if at least one recipient exists (non-empty string)
				recipients = [r for r in recipients if r]
				if recipients:
					send_mail(subject, message, getattr(settings, 'DEFAULT_FROM_EMAIL', None), recipients, fail_silently=True)
			except Exception:
				# don't break submission if email fails
				pass
			messages.success(request, 'Thanks for reaching out — your message has been received.')
			return redirect(reverse('pot:contact'))
	else:
		form = ContactForm()

	return render(request, 'pot/contact.html', {'form': form})


def faq(request):
	faqs = FAQ.objects.all().order_by('-created_at')
	return render(request, 'pot/faq.html', {'faqs': faqs})


def portfolio(request):
	projects = Project.objects.all().order_by('-created_at')
	return render(request, 'pot/portfolio.html', {'projects': projects})


def blog_list(request):
	posts = Post.objects.filter(published=True).order_by('-published_at', '-created_at')
	return render(request, 'pot/blog_list.html', {'posts': posts})


def blog_detail(request, slug):
	post = get_object_or_404(Post, slug=slug, published=True)
	return render(request, 'pot/blog_detail.html', {'post': post})
