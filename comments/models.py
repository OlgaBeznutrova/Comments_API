from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Comment(MPTTModel):
    text = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, null=True, on_delete=models.CASCADE, related_name="comments")
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    def __str__(self):
        return self.text

    class MPTTMeta:
        order_insertion_by = ["created_at"]
