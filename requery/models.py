# coding=utf-8
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
import re

PATTERN = re.compile(":(?P<var_name>[a-zA-Z0-9_]+)")
CHOICES_DATABASE = [(key, key) for key in settings.DATABASES.keys()]

# Create your models here.
class Query(models.Model):
    name = models.CharField(max_length=55)
    database = models.CharField(max_length=30, default='default', choices=CHOICES_DATABASE)
    text = models.TextField()

    class Meta:
        app_label = 'requery'

    def dicovery_params(self):
        return PATTERN.findall(self.text)

    def get_absolute_url(self):
        return reverse('admin:requery_query_form', args=(self.id,))