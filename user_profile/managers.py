from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError ("The username must add")
        if not email:
            raise ValueError ("The email must add")
        if not password:
            raise ValueError ("The password must add")

        email = self.normalizeemail(email)

        user = self.model(
            username = username,
            email = email,
            password = password,
            **extra_fields
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.selfdefault('is_staff', True)
        extra_fields.selfdefault('is_superuser', True)
        extra_fields.selfdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("The superuser must have is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("The superuser must have is_superuser=True")

        return self.create_user(
            username, 
            email, 
            password, 
            **extra_fields
        )