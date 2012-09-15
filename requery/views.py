# coding=utf-8
# Create your views here.
from django.contrib.admin.helpers import Fieldset
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.encoding import force_unicode
from requery.forms import QueryForm
from requery.models import Query
from django.conf import settings

def form_query(request, query_id):
    query = Query.objects.get(id=query_id)
    form = QueryForm(query=query)

    context = {
        'title': ('Run Query %s') % force_unicode(query.name),
        'form': form,
        'object_id': query_id,
        'original': query,
        'is_popup': "_popup" in request.REQUEST,
        'app_label': query._meta.app_label,
        'opts': query._meta,
        'change': False,
        }


    return render_to_response('requery/query.html', context, context_instance=RequestContext(request))