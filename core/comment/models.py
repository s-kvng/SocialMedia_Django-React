from django.db import models

# Create your models here.

from django.db import models

from core.abstract.models import AbstractModel , AbstractManager 

# Create your models here.

class CommentManager(AbstractManager):
    pass

class Comment(AbstractModel):
    post = models.ForeignKey('core_post.Post', related_name='post_comment', on_delete=models.PROTECT)
    author = models.ForeignKey('core_user.User', related_name='commented', on_delete=models.PROTECT)
    body = models.TextField()
    edited = models.BooleanField(default=False)

    objects = CommentManager()

    def __str__(self):
        return f"{self.author.name}"

    class Meta:
        db_table="'core_comment'"