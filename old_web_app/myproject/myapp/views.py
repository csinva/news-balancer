# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from myproject.myapp.models import Document
import random
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Document
from django.core.exceptions import *
import pickle
from train import normalize_text
from sklearn.feature_extraction.text import CountVectorizer  # function for encoding categories


def search(request):
    print('searching....')
    search_title = request.POST.get('textfield', None)
    print("search_id", search_title)
    nb = pickle.load(open("model.pkl", "rb"))
    vec = pickle.load(open("vocab.pkl", "rb"))

    '''
    print("nb", nb)
    tit = normalize_text(search_title)
    print("tit", tit)
    # vectorizer = CountVectorizer()
    # vectorizer.set_params(vocabulary=vocab)
    # x = vectorizer.fit_transform(tit)
    x = vec.fit_transform(tit)
    print("x.shape", x.shape)
    y = nb.predict(x)
    print("y", y)
    '''
    y = Document.objects.order_by('?').first().cluster

    # Load documents for the list page
    main_doc = Document(title=search_title, publisher="", link="",
                        cluster=y, bias=0, cred=1)
    tit1 = main_doc.title
    cluster = main_doc.cluster
    print('title', tit1)
    print('cluster', cluster)
    docs_remaining = Document.objects.filter(cluster=cluster).order_by('bias')
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
