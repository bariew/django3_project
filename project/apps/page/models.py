from datetime import datetime

from django.db import models

from project.apps.user import models as user_models


class Page(models.Model):
    title = models.CharField('title', max_length=256)
    content = models.TextField('content')
    created_at: datetime = models.DateTimeField()


class Comment(models.Model):
    page_id = models.ForeignKey(Page, on_delete=models.CASCADE)
    user_id = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    content = models.TextField('content')
    created_at: datetime = models.DateTimeField()
