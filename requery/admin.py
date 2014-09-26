# coding=utf-8
from django.conf.urls import url
from django.contrib import admin
from django.core.urlresolvers import reverse
from requery import views
from requery.models import Query
from requery import local_settings

try:
    import pygments
    from pygments import highlight
    from pygments.lexers import SqlLexer
    from pygments.formatters import HtmlFormatter
    from pygments.styles.vs import VisualStudioStyle
except ImportError as e:
    pygments = False


class QueryAdmin(admin.ModelAdmin):

    list_display = ('id', 'database', 'name', 'short_text', 'count_params', 'run')
    list_filter = ('database',)
    search_fields = ('name',)
    change_form_template = 'admin/requery/change_form_requery.html'

    if local_settings.SQL_STATEMENTS_NOT_ALLOWED:
        list_display += ('allow',)

    def short_text(self, query):
        if pygments:
            return highlight(query.text[:50], SqlLexer(), HtmlFormatter(style=VisualStudioStyle, noclasses=True))
        else:
            return query.text[:50]
    short_text.allow_tags = True

    def count_params(self, query):
        return len(query.dicovery_params())

    def allow(self, query):
        return query.is_allow()
    allow.boolean = True

    def get_urls(self):

        urls = super(QueryAdmin, self).get_urls()
        my_urls = [
            url(
                r'(?P<query_id>\d+)/running/',
                self.admin_site.admin_view(views.form_query),
                name='requery_query_form',
            ),url(
                r'(?P<query_id>\d+)/run/',
                self.admin_site.admin_view(views.run_query),
                name='requery_query_run',
            ),
        ]
        return my_urls + urls

    def run(self, query):
        if query.is_allow():
            return "<a href=%s>Run</a>" % reverse('admin:requery_query_form', args=(query.id,))
        return "<a href=%s>View</a>" % reverse('admin:requery_query_form', args=(query.id,))
    run.short_description = "Run"
    run.allow_tags = True


admin.site.register(Query, QueryAdmin)

