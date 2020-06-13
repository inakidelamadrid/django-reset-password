from datetime import date

USER_CATEGORIES_REQUIRING_RESET = ["is_staff"]
RESET_PASSWORD_DELTA = 30


def calculate_days_passed(last_password_update_at, target=date.today()):
    return (target - last_password_update_at).days


def password_has_due_date(password_details):
    last_password_update_at = password_details.password_last_updated_at
    return calculate_days_passed(last_password_update_at) > RESET_PASSWORD_DELTA


def password_due(user):
    return not hasattr(user, "password_details") or password_has_due_date(user.password_details)


def should_reset_password(user):
    return (
        user.is_authenticated
        and any(
            [getattr(user, category) for category in USER_CATEGORIES_REQUIRING_RESET]
        )
        and password_due(user)
    )
