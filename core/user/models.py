import uuid

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from core.abstract.models import AbstractModel, AbstractManager

# Create your models here.


class UserManager(BaseUserManager, AbstractManager):
    # def get_object_by_public_id(self, public_id):
    #     try:
    #         instance = self.get(public_id=public_id)
    #         return instance
    #     except (ObjectDoesNotExist, ValueError, TypeError):
    #         return Http404

    def create_user(self, username, email, password, first_name, last_name, **kwargs):
        """_summary_
        create and return User
        Args:
            username (_type_): _description_
            email (ktu email): _description_
            password (_type_): _description_
        """

        if username is None:
            raise TypeError("User must have a username")
        if email is None:
            raise TypeError("User must have an email .")
        if password is None:
            raise TypeError("User must have a password.")
        if first_name is None:
            raise TypeError("User must have a first name")
        if last_name is None:
            raise TypeError("User must have a last name")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
        self, username, email, password, first_name, last_name, **kwargs
    ):
        """
        create and return User with superuser (admin) permissions
        """

        if username is None:
            TypeError("Superuser must have a username.")
        if email is None:
            TypeError("Superuser must have an email")

        # using the create_user method
        superuser = self.create_user(
            username, email, password, first_name, last_name, **kwargs
        )
        superuser.is_superuser = True
        superuser.is_staff = True

        superuser.save(self._db)

        return superuser


class User(AbstractBaseUser, PermissionsMixin, AbstractModel):
    # public_id = models.UUIDField(
    #     db_index=True, unique=True, default=uuid.uuid4, editable=False
    # )
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField(null=True)
    posts_liked = models.ManyToManyField("core_post.Post", related_name="liked_by")
    avatar = models.ImageField(null=True, blank=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    # instaniate the custom manager
    objects = UserManager()

    def like(self , post):
        """like a post if it hasn't been liked yet """
        return self.posts_liked.add(post)

    def remove_like(self , post):
        """unlike if `post` has already been liked by user """
        return self.posts_liked.remove(post)

    def has_liked(self , post ):
        """Return True if user has liked a post ; else false"""
        return self.posts_liked.filter(pk=post.pk).exists()

    def __str__(self):
        return f"{self.email}"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
