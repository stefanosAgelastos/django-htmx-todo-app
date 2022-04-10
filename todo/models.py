from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    text = models.TextField()
    rank = models.IntegerField(db_index=True)

    class Meta:
        ordering = ['rank']

    @classmethod
    def create(cls, title=title, text=text):
        cls.objects.create(
            title=title,
            text=text,
            rank=cls.highest_rank + 1)

    @classmethod
    @property
    def highest_rank(cls):
        return int(cls.objects.all().aggregate(models.Max('rank'))['rank__max'] or 1)

    # def rerank(self, new_rank):
