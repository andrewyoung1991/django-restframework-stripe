DEBUG = True

SECRET_KEY = "unguessable"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "restframework_stripe",
    ]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "travis_ci_test",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "localhost"
        }
    }

RESTFRAMEWORK_STRIPE = {
    "api_key": "xxxTESTINGxxx",
    "api_version": "2015-10-16"
    }

ROOT_URLCONF = "tests.urls"
SITE_ID = 1

MIDDLEWARE_CLASSES = (
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "restframework_stripe.middleware.CustomerMerchantMiddleware",
    )
