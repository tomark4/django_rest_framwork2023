from django.db import models
from users.models import User
from posts.models import Post


class Comment(models.Model):
  text = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)

  def __str__(self):
    return self.text