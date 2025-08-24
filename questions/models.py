from django.db import models

# Create your models here.

class Question(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
