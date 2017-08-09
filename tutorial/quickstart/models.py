from django.db import models

# Create your models here.

class UserTest(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()

class Entry(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
        (STATUS_DRAFT, "草稿"),
        (STATUS_PUBLIC, "公开"),
    )
    title  = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
    author = models.ForeignKey(UserTest, related_name='entries')
