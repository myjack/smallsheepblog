#!/usr/bin/python
#coding:utf-8

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

#show index page
def index(request):
    return render_to_response('index.html',{},context_instance = RequestContext(request))

#show sub page
def subPage(request):
    return render_to_response('view.html',{},context_instance = RequestContext(request))


