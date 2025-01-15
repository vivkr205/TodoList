from django.db import models
from django.contrib.auth.models import User

class Tasklist(models.Model):
    # options=[
    #     ('Done','Done'),
    #     ('Not Done','Not Done')
    # ]
    id= models.AutoField(primary_key=True)
    manage_id=models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task=models.CharField(max_length=300)
    done=models.BooleanField(default=False)
    def __str__(self):
        return self.task+"-"+str(self.done)
