from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from ckeditor.fields import RichTextField

class Entry(models.Model):
    Title = models.CharField(max_length=100)
    Journal = RichTextField(blank=False)
    Date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title
