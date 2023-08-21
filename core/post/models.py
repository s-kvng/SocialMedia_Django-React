from django.db import models
from django.contrib.auth.models import PermissionsMixin

from abstract.models import AbstractModel
from user.models import User

# Create your models here.


class PostManager:
    pass


class Post(AbstractModel):
    # this ForeignKey makes it symmetrical , meaning I can query using Post.author and also use User.post_set
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=False)

    objects = PostManager()

    def __str__(self):
        return {self.author.name}

    class Meta:
        db_name = "'core.post'"
