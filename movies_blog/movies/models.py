from django.db import models

# 클래스명은 테이블 이름 
class Movie(models.Model):
    # 각 변수값은 필드명 
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_open = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
