from django.db import models
from django.urls import reverse
from django.utils.text import slugify #it removes spaces from a string and add - in place so that we can use that string as url
import misaka # it is used for link embadding with string
from django.contrib.auth import get_user_model # it retyurns user model that is a tive in this project. which allows to call things off of current user session.

User = get_user_model()
# Create your models here.

from django import template
register = template.Library()


class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    members = models.ManyToManyField(User,through='GroupMember') #one user can be a member of many groups as well as one group can have many users i.e. manytomany relationship

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})

    class Meta():
        ordering = ['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta():
        unique_together = ('user','group')
