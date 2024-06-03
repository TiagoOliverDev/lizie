import django
from django.conf import settings
from django.db import connections
from django.db.utils import OperationalError

# Configure settings for standalone Django script
settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }
)

django.setup()

# Test the connection
db_conn = connections['default']
try:
    db_conn.ensure_connection()
    print("Database connection successful!")
except OperationalError:
    print("Database connection failed!")
