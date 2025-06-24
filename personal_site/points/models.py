from django.db import models
from taggit.managers import TaggableManager

class Section(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    tags = TaggableManager()

    def __srt__(self):
        return self.title

class Point(models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name='points'
    )

    title = models.CharField(max_length=500)
    description = models.TextField()
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return f"{self.section.title} - {self.title}"

class BulletPoint(models.Model):
    point = models.ForeignKey(
        Point,
        on_delete=models.CASCADE,
        related_name='bulletpoints'
    )
    sentence = models.TextField()
    tags = TaggableManager()

    def __str__(self):
        return f"{self.point.title} - {self.sentence[:50]}"
