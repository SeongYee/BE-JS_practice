from django.db import models

# Create your models here.
class Article(models.Model):
    #각 변수값은 필드명
    title = models.CharField(max_length=20)
    content = models.TextField()

    is_open = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
