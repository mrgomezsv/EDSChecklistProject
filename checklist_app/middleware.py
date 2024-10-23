from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth import logout

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            now = datetime.now()

            if last_activity:
                elapsed_time = now - datetime.strptime(last_activity, '%Y-%m-%d %H:%M:%S.%f')
                if elapsed_time.total_seconds() > settings.SESSION_COOKIE_AGE:
                    logout(request)
            request.session['last_activity'] = str(now)

        response = self.get_response(request)
        return response
