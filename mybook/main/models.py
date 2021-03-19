from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from random import randint

class Entry(models.Model):
    Title = models.CharField(max_length=100)
    Journal = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):
        if Entry.objects.filter(Title=self.Title).exists():
            extra = str(randint(0, 900000))
            self.slug = slugify(self.Title) + "-" + extra
        else:
            self.slug = slugify(self.Title)
        super(Entry, self).save(*args, **kwargs)




    def __str__(self):
        return self.Title
