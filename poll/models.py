from datetime import datetime
from django.db import models


class Poll(models.Model):

    question = models.TextField()
    option_1 = models.CharField(max_length=30)    
    option_2 = models.CharField(max_length=30)    
    option_3 = models.CharField(max_length=30)    
    option_1_count = models.IntegerField(default=0) 
    option_2_count = models.IntegerField(default=0) 
    option_3_count = models.IntegerField(default=0) 
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def total_votes(self):

        return self.option_1_count + self.option_2_count + self.option_3_count
