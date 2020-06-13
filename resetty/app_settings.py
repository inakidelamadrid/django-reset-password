from django.conf import settings

USER_CATEGORIES_REQUIRING_RESET =  getattr(settings, 'RESETTY_USER_CATEGORIES_REQUIRING_RESET', ['is_staff'])
RESET_PASSWORD_DELTA = getattr(settings, 'RESETTY_RESET_PASSWORD_DELTA',  30)
