from django.db import models

class Info (models.Model):
    key = models.IntegerField ()
    val = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{}".format(self.key)

