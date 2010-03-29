#!/usr/bin/python
# -*- coding: utf-8 -*-
# req_log/middleware.py
""" Reqest log middleware """

from models import RequestLog
import types


class RequestLogMiddleware(object):
    """Middleware that gets various objects from the
    request object and saves them in thread local storage."""

    log = {}

    def process_request(self, request):
        """Process request to middleware"""
        self.log["path"] = request.path
        self.log["method"] = request.method
        self.log["encoding"] = request.encoding
        self.log["get"] = request.GET
        self.log["post"] = request.POST
        self.log["meta"] = dict(filter(lambda item: isinstance(item[1],
                              types.StringTypes), request.META.items()))
        self.log["cookies"] = request.COOKIES
        if bool(request.FILES):
            self.log["files"] = {"name": request.FILES.name,
                                 "size": request.FILES.size}
        else:
            self.log["files"] = {}

    def process_view(self, request, view_func, view_args, view_kwargs):
        if hasattr(self,"log"):
            self.log["view"] = "%s:%s" % (view_func.__module__,
                                         view_func.__name__)
            self.log["view_args"] = view_args
            self.log["view_kwargs"] = view_kwargs 
        
        
        
    def process_response(self, request, response):
        if hasattr(self,"log"):
            self.log["response_status"] = response.status_code
            RequestLog.objects.create(**self.log)
        return response
