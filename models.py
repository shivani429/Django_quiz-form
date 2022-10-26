from django.db import models
from datetime import datetime

class QuizModel(models.Model):
    question = models.CharField(max_length = 250)
    option1 = models.CharField(max_length=250)
    option2 = models.CharField(max_length=250)
    option3 = models.CharField(max_length=250)
    option4 = models.CharField(max_length=250)
    ans = models.CharField(max_length=250)
    def __str__(self):
        return self.question


  





