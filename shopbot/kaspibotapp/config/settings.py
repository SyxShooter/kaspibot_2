# settings.py

import os

# Define your project's base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: Keep this key secret in production!
SECRET_KEY = 'your-secret-key'

# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = True

# Add your bot's IP address or domain to the list of allowed hosts
ALLOWED_HOSTS = ['your-bot-domain.com', 'localhost']

# Application definition
INSTALLED_APPS = [
    # Add your project's apps here
    'bot',
    # ...
]

# Middleware
MIDDLEWARE = [
    # ...
]

# Database settings (configure as needed)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Configure your web scraping settings
WEB_SCRAPER_INTERVAL = 180  # Adjust the interval in seconds for your scraping needs

# Other project-specific settings
# ...

# Add any sensitive information (e.g., API keys) to a separate settings file
try:
    from local_settings import *
except ImportError:
    pass
