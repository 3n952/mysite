from django.db import models
from django.utils import timezone
# Create your models here.

# DATABASE 모델 2가지
# 
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date publushed')

    def __str__(self):
        return self.question_text
    
    def was_publushed_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    #선택지에 해당하는 질문 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
