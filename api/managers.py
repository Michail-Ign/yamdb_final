from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, **kwargs):
        if not email:
            raise ValueError('Почта должна быть указана')
        if username is None:
            username = email
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username
        )
        user.save()
        return user

    def create_superuser(self, email, password, username, **kwargs):
        if password is None:
            raise TypeError('Superuser must have a password.')
        user = self.model(
            email=email,
            username=username
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
