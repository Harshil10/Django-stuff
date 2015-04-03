import os
import sys
from datetime import datetime, timedelta
from django.conf import settings

class InactivityLogout(object):
        def process_request( self, request ):
                COOKIE_AGE = getattr(settings, 'SESSION_COOKIE_AGE', 900)
                if datetime.now() - request.session.get_expiry_date() < timedelta(seconds = COOKIE_AGE):
                        request.session.set_expiry(datetime.now() + timedelta(seconds = COOKIE_AGE))
                return None # pass through
