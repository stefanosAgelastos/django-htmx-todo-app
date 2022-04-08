from django.db import models


class Todo(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return f'{self.question_text} - {self.pub_date}'
