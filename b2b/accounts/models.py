from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from datetime import datetime

class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email')

        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)  # Save to ensure `id` is generated
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username=username, email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Profile(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=20, unique=True, blank=True, editable=False)
    username = models.CharField(max_length=20, unique=True, blank=False)
    email = models.EmailField(max_length=254, unique=True, blank=False)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    stans = models.IntegerField(default=0, blank=True)
    stanning = models.IntegerField(default=0, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=True)
    
    groups = models.ManyToManyField(Group, related_name='account_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='account_set', blank=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'birth_date']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def follow(self, profile):
        self.followers.add(profile)
        self.stanning += 1
        profile.stans += 1
        self.save()
        profile.save()

    def unfollow(self, profile):
        self.followers.remove(profile)
        self.stanning -= 1
        profile.stans -= 1
        self.save()
        profile.save()

    def generate_user_id(self):
        user_first_initial = self.username[0].upper() if self.username else 'X'
        user_last_initial = self.username[0].lower() if self.username else 'X'
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        return f"{user_first_initial}{user_last_initial}{timestamp}"

    def save(self, *args, **kwargs):
        # Ensure `user_id` is only generated if missing
        if not self.user_id:
            self.user_id = self.generate_user_id()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        ordering = ['user_id']
