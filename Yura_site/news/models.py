from django.db import models

class Article(models.Model):
    """Стаття що буде розміщуватись у розділі 'новини'"""
    name = models.CharField('Назва статті', max_length=255)

    class Meta:
        db_table = 'case'
