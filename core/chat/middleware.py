from django.utils.timezone import now
from django.contrib.auth.middleware import get_user
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import uuid

class UpdateLastSeenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            user = get_user(request)
        except ValidationError:
            # Clear invalid session data (integer ID instead of UUID)
            if request.session.get('_auth_user_id'):
                del request.session['_auth_user_id']
                request.session.modified = True
            user = get_user(request)
        
        if user.is_authenticated:
            user.profile.last_seen = now()
            user.profile.save(update_fields=['last_seen'])
        return self.get_response(request)
