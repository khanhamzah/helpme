from operator import truediv
from django.db import models

class User(models.Model) :
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

class Posts(models.Model):
   postContent = models.TextField()
   postAuthor = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model) :
    postId = models.ForeignKey(Posts, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)

# class Chats(models.Model) :
#     chatId = models.ForeignKey(Posts, on_delete=models.CASCADE)
#     helpers = models.ForeignKey(User, on_delete=models.CASCADE)