from django.db import models


class bookStore(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.CharField(max_length=500,null=True)
    name = models.CharField(max_length=200,null=True)
    stock = models.IntegerField(default=0,null=True)

    added_at = models.DateTimeField(null=True)
    modified_at = models.DateTimeField(null=True)