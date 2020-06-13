from datetime import date
from django.http import HttpResponseRedirect

from .http import reset_password_redirect_url
from .models import ResetPasswordExtra

USER_CATEGORIES_REQUIRING_RESET = ["is_staff"]


def password_due(user):
    return not hasattr(user, "password_details")


def should_reset_password(user):
    return (
        user.is_authenticated
        and any(
            [getattr(user, category) for category in USER_CATEGORIES_REQUIRING_RESET]
        )
        and password_due(user)
    )


class ResetPasswordMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if should_reset_password(request.user) and not request.path.startswith('/accounts/reset/'):
            return HttpResponseRedirect(reset_password_redirect_url(request.user))

        # the code above happens before subsequent middlewares in the stack and response

        response = self.get_response(request)

        # the code below will happen after response and previous middlewares in the stack

        return response
