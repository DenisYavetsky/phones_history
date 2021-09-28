from django.db import models
import hashlib


class CustomUsers(models.Model):
    user_login = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=40, blank=False)

    def generate_password_hash(self):
        return hashlib.sha1(self.password.encode()).hexdigest()

    def check_password(self, password: str) -> bool:
        return self.password == hashlib.sha1(password.encode()).hexdigest()

    def restore_password(self):
        pass

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.password = self.generate_password_hash()
        super().save()
