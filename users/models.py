from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, models.CASCADE)

    # additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    # https://stackoverflow.com/a/24936834/4449743
    # activation_key = models.CharField(max_length=40)
    # key_expires = models.DateTimeField()

    def __str__(self):
        return self.user.username
