from django.db import models
from django_summernote.fields import SummernoteTextField
import datetime

class Author(models.Model):
    """Автор, що пише статті"""
    name = models.CharField('Ім\'я автора', max_length=100)
    lastName = models.CharField('Прізвище автора', max_length=100)
    email = models.CharField('Електрона пошта', max_length=255)
    def __str__(self):
        return self.name + ' ' + self.lastName
    def __unicode__(self):
        return self.name + ' ' + self.lastName

class Article(models.Model):
    """Стаття що буде розміщуватись у розділі 'новини'"""
    name = models.CharField('Назва статті', max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateField(default=datetime.date.today, blank=True)
    # def __str__(self):
    #     return self.name + " ==> " + str(self.author)
    #
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name + "-" + str(self.post_date))
    #     return super().save(*args, **kwargs)
