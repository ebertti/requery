# coding=utf-8
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
import re
from requery.local_settings import SQL_STATEMENTS_NOT_ALLOWED

PATTERN = re.compile(":(?P<var_name>[a-zA-Z0-9_]+)")
CHOICES_DATABASE = [(key, key) for key in settings.DATABASES.keys()]


class Query(models.Model):
    name = models.CharField(max_length=55)
    database = models.CharField(max_length=30, default='default', choices=CHOICES_DATABASE)
    text = models.TextField()

    def __unicode__(self):
        return self.name

    def dicovery_params(self):
        return PATTERN.findall(self.text)

    def get_absolute_url(self):
        return reverse('admin:requery_query_form', args=(self.id,))

    def prepare_text(self):
        params = self.dicovery_params()
        prepared = self.text
        for param in params:
            prepared = prepared.replace(':%s' % param, '%s')

        return prepared

    def is_allow(self):
        for statement in SQL_STATEMENTS_NOT_ALLOWED:
            if re.match('\s*' + statement + '\s', self.text, re.IGNORECASE):
                return False
        return True