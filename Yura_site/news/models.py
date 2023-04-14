from django.db import models
import datetime

class Author(models.Model):
    """Автор, що пише статті"""
    name = models.CharField('Ім\'я автора', max_length=100)
    lastName = models.CharField('Прізвище автора', max_length=100)
    email = models.CharField('Електрона пошта', max_length=255)


class Article(models.Model):
    """Стаття що буде розміщуватись у розділі 'новини'"""
    name = models.CharField('Назва статті', max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.CharField('Текст статті', max_length=90000)
    date = models.DateField(default=datetime.date.today, blank=True)
