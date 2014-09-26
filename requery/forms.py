# coding=utf-8
from django import forms
from django.forms.util import ErrorList


class QueryForm(forms.Form):
    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=':', empty_permitted=False, query=None):

        super(QueryForm, self).__init__(data, files, auto_id, prefix, initial, error_class, label_suffix,
            empty_permitted)
        self.query = query
        if self.query :
            for param in self.query.dicovery_params():
                self.fields[param] = forms.CharField()

