from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def reset_password_redirect_url(user, token_generator=default_token_generator):
    path_params = {
        "uidb64": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": token_generator.make_token(user),
    }
    return reverse("password_reset_confirm", kwargs=path_params)
