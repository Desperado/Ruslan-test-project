from models import RequestLog
import types
class RequestLogMiddleware(object):
    log = {}
    def process_request(self, request):
        
        self.log["path"] = request.path
        self.log["method"] = request.method
        self.log["encoding"] = request.encoding
        self.log["get"] = request.GET
        self.log["post"] = request.POST
        #saving only string type meta 
        self.log["meta"] = dict(filter(lambda item: isinstance(item[1],types.StringTypes),
                                       request.META.items()))
        self.log["cookies"] = request.COOKIES
        if bool(request.FILES):
            self.log["files"] = {"name":request.FILES.name,
                                 "size":request.FILES.size}
        else:
            self.log["files"] = {}
    def process_view(self, request, view_func, view_args, view_kwargs):
        self.log["view"] = "%s:%s"%(view_func.__module__,
                                    view_func.__name__)
        self.log["view_args"] = view_args
        self.log["view_kwargs"] = view_kwargs 
        
    def process_response(self, request, response):
        self.log["response_status"] = response.status_code
        RequestLog.objects.create(**self.log)
        return response

