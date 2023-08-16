from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Notes(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200,default="")
    notes = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='notes')

    def __str__(self):
        return self.title
