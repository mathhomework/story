from django.contrib.auth.models import AbstractUser
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.



class Writer(AbstractUser):
    pass


class Branch(MPTTModel):
    title = models.CharField(max_length = 120)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    user = models.ForeignKey(Writer)
    text = models.TextField()

    class MPTTMeta:
        order_insertion_by = ['title']

    def __unicode__(self):
        return u"{}".format(self.title)

class Vote(models.Model):
    writer_vote = models.ForeignKey(Writer)
    branch_vote = models.ForeignKey(Branch)

