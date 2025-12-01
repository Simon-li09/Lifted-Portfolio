Development
-----------

Create a virtual environment, install dependencies (if any), and run migrations:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
python -m pip install -r requirements.txt || echo "Install dependencies if you have any"
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_pot  # optional: seed sample About, FAQ, Projects
python manage.py runserver
```

The site will be available at http://127.0.0.1:8000/ and admin at /admin/.

Email
-----

By default the project uses console email backend for development. To enable SMTP, set the following in `main/settings.py` (or via environment variables):

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'user@example.com'
EMAIL_HOST_PASSWORD = 'securepassword'
DEFAULT_FROM_EMAIL = 'webmaster@example.com'
ADMINS = [('Admin', 'admin@example.com')]
```

The contact form stores messages to `Contact` model which you can view in Django admin.

