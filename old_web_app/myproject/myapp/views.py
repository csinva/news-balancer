# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from myproject.myapp.models import Document
import random


def list(request):
    # Load documents for the list page
    documents = Document.objects.all()
    main_doc = Document.objects.order_by('?').first()
    tit1 = main_doc.title
    cluster = main_doc.cluster
    print('title', tit1)
    print('cluster', cluster)
    docs_remaining = Document.objects.exclude(title=tit1).filter(cluster=cluster).order_by('bias')
    docs_count_3 = docs_remaining.count() / 3
    # objs = sorted(qs, key=lambda o: o.some_other_field)
    docs_lib = docs_remaining[:docs_count_3]

    docs_lib = sorted(docs_lib,
                      key=lambda x: -1 * (x.cred - 1e6) if x.cred < 10
                      else (-1 * x.cred + random.randint(0, 15) if x.cred < 40
                            else -(x.cred + 1e6)))
    docs_mid = sorted(docs_remaining[docs_count_3:2 * docs_count_3],
                      key=lambda x: -1 * (x.cred - 1e6) if x.cred < 10
                      else (-1 * x.cred + random.randint(0, 15) if x.cred < 40
                            else -(x.cred + 1e6)))
    docs_cons = sorted(docs_remaining[2 * docs_count_3:3 * docs_count_3],
                       key=lambda x: -1 * (x.cred - 1e6) if x.cred < 10
                       else (-1 * x.cred + random.randint(0, 15) if x.cred < 40
                             else -(x.cred + 1e6)))
    print('num_docs_remaining', docs_count_3)
    # Render list page with the documents and the form
    return render_to_response(
        'myapp/list.html',
        {'main_doc': main_doc, 'docs_lib': docs_lib, 'docs_mid': docs_mid,
         'docs_cons': docs_cons},
        context_instance=RequestContext(request)
    )
