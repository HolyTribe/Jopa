from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """Пользовательский менеджер"""

    def create_user(self, email, password, **extra_fields):
        """Создание пользователя"""
        if not email:
            raise ValueError("Нужно установить email")
        # Очистка емейла
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Создание суперпользователя"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Нужно установить is_staff для суперпользователя")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Нужно установить is_superuser для суперпользователя")
        return self.create_user(email, password, **extra_fields)
