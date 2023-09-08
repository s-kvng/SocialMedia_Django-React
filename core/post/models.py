from django.db import models
from django.contrib.auth.models import PermissionsMixin

from core.abstract.models import AbstractModel, AbstractManager

# from user.models import User

# Create your models here.


class PostManager(AbstractManager):
    pass


class Post(AbstractModel):
    # this ForeignKey makes it symmetrical , meaning I can query using Post.author and also use User.post_set
    #post_set attribute contains all the instructions needed to interact with all the posts linked to this user
    author = models.ForeignKey(to="core_user.User", on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=False)

    objects = PostManager()

    def __str__(self):
        return f"{self.author.name}"

    class Meta:
        db_table = "'core.post'"
