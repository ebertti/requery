# coding=utf-8
# Create your views here.
import json
import six
from django.conf import settings
from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.defaultfilters import safe
if six.PY3:
    from django.utils.encoding import force_text
else:
    from django.utils.encoding import force_unicode as force_text
from requery.forms import QueryForm
from requery.models import Query
from django.db import connections


def form_query(request, query_id):
    query = Query.objects.get(id=query_id)
    form = QueryForm(initial={'text':query.text}, query=query)
    context = {
        'title': 'Run Query %s on database %s' % (force_text(query.name), query.database),
        'form': form,
        'object_id': query_id,
        'original': query,
        'media': safe("""<script type="text/javascript" src="{0}admin/js/core.js"></script>
                    <script type="text/javascript" src="{0}admin/js/jquery.js"></script>
                    <script type="text/javascript" src="{0}admin/js/jquery.init.js"></script>""".format(settings.STATIC_URL)),
        'is_popup': "_popup" in request.REQUEST,
        'app_label': query._meta.app_label,
        'opts': query._meta,
        'change': False,
        }
    return render_to_response('requery/query.html', context, context_instance=RequestContext(request))


def run_query(request, query_id):
    query = Query.objects.get(id=query_id)
    if query.is_allow():
        text = query.prepare_text()
        params = []
        for param in query.dicovery_params():
            params.append(request.POST[param])

        cursor = connections[query.database].cursor()
        cursor.execute(text, params)
        lines = []
        for line in cursor.fetchall():
            lines.append([six.text_type(tup) for tup in line])

        if lines :
            response = {
                'template': '#table-response',
                'columns': [col[0] for col in cursor.description],
                'lines': lines
            }
        else:
            response = {
                'template' : '#message-response',
                'message' : 'No data'
            }
        cursor.close()
        LogEntry(user=request.user,
                 content_type=ContentType.objects.get_for_model(query),
                 object_id=query.id,
                 object_repr=force_text(query),
                 change_message="run with %s" % ', '.join(['%s:%s' % (key, value)
                                                 for key, value in request.POST.items()
                                                 if key != 'csrfmiddlewaretoken']),
                 action_flag=2 #change
        ).save()
        return HttpResponse(json.dumps(response), content_type="application/json")

    return HttpResponseForbidden()
