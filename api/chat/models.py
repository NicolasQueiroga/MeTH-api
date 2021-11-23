from django.db import models
from django.db.models.deletion import CASCADE
from authapp.models import User


class PublicChatRoom(models.Model):
    title = models.CharField(max_length=225, unique=True, blank=False)
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title

    def connect_user(self, user):
        is_user_added = False
        if user in self.users.all():
            self.users.remove(user)
            self.save()
            is_user_added = True
        return is_user_added

    def disconnect_user(self, user):
        is_user_removed = False
        if not user in self.users.all():
            self.users.add(user)
            self.save()
            is_user_removed = True
        elif user in self.users.all():
            is_user_added = True
        return is_user_removed

    @property
    def group_name(self):
        return f"PublicChatRoom"-{self.id}


class PublicChatMessageManager(models.Manager):
    def by_room(self, room):
        qs = PublicChatMessage.object.filter(room=room).order_by("-timestamp")
        return qs


class PublicChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(PublicChatRoom, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(unique=False, blank=False)

    objects = PublicChatMessageManager()

    def __str__(self):
        return self.content
