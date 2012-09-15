# coding=utf-8
# Create your views here.
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.defaultfilters import safe
from django.utils.encoding import force_unicode
from requery.forms import QueryForm
from requery.models import Query
from django.db import connections
from django.utils import simplejson
import time

def form_query(request, query_id):
    query = Query.objects.get(id=query_id)
    form = QueryForm(initial={'text':query.text}, query=query)
    context = {
        'title': ('Run Query %s on %s') % (force_unicode(query.name), query.database),
        'form': form,
        'object_id': query_id,
        'original': query,
        'media': safe("""<script type="text/javascript" src="/static/admin/js/core.js"></script>
                    <script type="text/javascript" src="/static/admin/js/jquery.js"></script>
                    <script type="text/javascript" src="/static/admin/js/jquery.init.js"></script>"""),
        'is_popup': "_popup" in request.REQUEST,
        'app_label': query._meta.app_label,
        'opts': query._meta,
        'change': False,
        }
    return render_to_response('requery/query.html', context, context_instance=RequestContext(request))

def run_query(request, query_id):
    query = Query.objects.get(id=query_id)
    text = query.prepare_text()
    params = []
    for param in query.dicovery_params():
        params.append(request.POST[param])

    cursor = connections[query.database].cursor()
    cursor.execute(text, params)
    lines = []
    for line in cursor.fetchall():
        lines.append([unicode(tup) for tup in line])

    if lines :
        response = {
            'template' : '#table-response',
            'columns' : [col[0] for col in cursor.description],
            'lines' : lines
        }
    else:
        response = {
            'template' : '#message-response',
            'message' : 'No data'
        }
    cursor.close()
    return HttpResponse(simplejson.dumps(response), mimetype='application/json')
