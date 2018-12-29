from flask import current_app
from app.email import send_mail


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_mail(
        '[First Flask App] Reset Your Password',
        sender=current_['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('email/reset_password.txt', user=user, token=token),
        html_body=render_template('email/reset_password.html', user=user, token=token)
    )