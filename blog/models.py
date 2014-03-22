from django.db import models

class Post(models.Model):

    def __unicode__(self):
        return self.title

    title = models.CharField(max_length=255, default="A Post without Name ;(")
    content = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)