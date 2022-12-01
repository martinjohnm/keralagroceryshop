import email
from . models import Accounts
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

class AccountsBackend(BaseBackend):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """

    def authenticate(self, request, username=None, password=None):
        
            try:
                user = Accounts.objects.get(email=username)
                success = user.check_password(password)
                if success:
                    return user
            except Accounts.DoesNotExist:
                return None

    def get_user(self, user_id):
        try:
            return Accounts.objects.get(pk=user_id)
        except Accounts.DoesNotExist:
            return None