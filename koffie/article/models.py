from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    link = models.CharField(max_length=2000)
    name = models.CharField(max_length=200, blank=True)
    added_date = models.DateTimeField('date added', auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True, through='Article_Tags')
    added_by = models.ForeignKey(User, related_name='added_by')

    votes_up = models.IntegerField(default=1)
    votes_down = models.IntegerField(default=0)

    def nice_name(self):
        return self.__unicode__()
    nice_name.short_description = "name"

    def list_tags(self):
        return self.tags.all()

    def all_tags(self):
        return ', '.join([tag.name for tag in self.tags.all()])

    def __unicode__(self):
        if not self.name: 
            return self.link
        else:
            return self.name


class Article_Tags(models.Model):
    article = models.ForeignKey(Article)
    tag = models.ForeignKey(Tag)
    #count = models.IntegerField(default=1)

