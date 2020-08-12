from django.db import models

# Create your models here.
class Todolist(models.Model):
    name = models.CharField(max_length=200, verbose_name='Title', help_text='Enter a title of list')
    text = models.TextField(null=True, blank=True, verbose_name='Text')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')
    organization = models.ForeignKey('Organization', null=True, on_delete=models.PROTECT, verbose_name='Organization')
    company = models.CharField(max_length=200, verbose_name='Company')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'ToDo lists'
        verbose_name = 'ToDo list'
        ordering = ['published']


class Organization(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Organization')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Organizations'
        verbose_name = 'Organization'