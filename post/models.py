from django.db import models

# Create your models here.

class Category(models.Model):
  text = models.CharField(max_length=100)

  def __str__(self):
    return self.text

class Post(models.Model):
  title = models.TextField()
  content = models.TextField()
  category = models.ForeignKey('Category', related_name="posts", on_delete=models.CASCADE)
  create_at = models.DateTimeField(auto_now_add=True)

  user = models.ForeignKey('auth.user', related_name="posts", on_delete=models.CASCADE)

  def __str__(self):
    return self.title