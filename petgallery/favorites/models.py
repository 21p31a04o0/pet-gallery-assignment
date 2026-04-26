from django.db import models

from django.contrib.auth.models import User
class Favorite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image_url=models.URLField()
    breed=models.CharField(max_length=100,blank=True,null=True)
    notes=models.TextField(blank=True,null=True)
    tags=models.JSONField(default=list,blank=True)
    def __str__(self):
        return self.breed if self.bread else "Favorite"
