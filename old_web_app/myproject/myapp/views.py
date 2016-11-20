# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm


def list(request):
    # Load documents for the list page
    documents = Document.objects.all()
    main_doc = Document.objects.order_by('?').first()
    tit1 = main_doc.title
    cluster = main_doc.cluster
    print('title', tit1)
    print('cluster', cluster)
    docs_remaining = Document.objects.exclude(title=tit1).filter(cluster=cluster)
    print('num_docs_remaining', len(docs_remaining))
    # Render list page with the documents and the form
    return render_to_response(
        'myapp/list.html',
        {'documents': documents, 'main_doc': main_doc, 'docs_remaining': docs_remaining},
        context_instance=RequestContext(request)
    )
