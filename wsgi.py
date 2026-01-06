import os
import sys

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
core_path = os.path.join(project_root, 'core')
if core_path not in sys.path:
    sys.path.insert(0, core_path)

# Set Django settings module to core.core.settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
