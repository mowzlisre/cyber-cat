from django.db import models
from users.models import User
from ckeditor.fields import RichTextField


class Tutorials(models.Model):
    chapter = models.CharField(max_length=50)
    description = models.TextField()
    content = RichTextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chapter

class Subject(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    tutorials = models.ManyToManyField(Tutorials, related_name='tutorials+')
    students = models.ManyToManyField(User, related_name='students+')
    sub_name = models.CharField(max_length=20, blank=True)

    def save(self):
        self.sub_name = self.name.lower()
        return super(Subject, self).save()

    def __str__(self):
        return self.name